u"""Módulo View Cita."""

from apps.utils.decorators import permission_resource_required
from apps.utils.security import get_dep_objects, log_params, SecurityKey
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.utils.encoding import force_text
from django.utils.text import capfirst
from django.utils.translation import ugettext as _
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView

from ..models.cita import Cita
from ..forms.cita import CitaForm
from django.core import serializers
from django.http import HttpResponse
from ..models.eventos import Evento
import json

import logging
log = logging.getLogger(__name__)


class CitaView(TemplateView):
    u"""Cita."""
    template_name = "cita/index.html"

    @method_decorator(permission_resource_required)
    def dispatch(self, request, *args, **kwargs):
        """dispatch."""
        return super(CitaView,
                     self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Cita ListView List get context.
        """
        context = super(CitaView,
                        self).get_context_data(**kwargs)
        context['title'] = ('Seleccione %s para editar'
                            ) % capfirst('Cita')
        return context


class CitaCreateView(CreateView):
    u"""Cita."""

    model = Cita
    form_class = CitaForm
    template_name = "cita/form.html"
    success_url = reverse_lazy("citas:cita_add")

    @method_decorator(permission_resource_required)
    def dispatch(self, request, *args, **kwargs):
        """dispatch."""
        return super(CitaCreateView,
                     self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Cita ListView List get context.

        Funcion con los primeros datos iniciales para la carga del template.
        """
        context = super(CitaCreateView,
                        self).get_context_data(**kwargs)
        context['opts'] = self.model._meta
        # context['cmi'] = 'tipodoc'
        context['title'] = ('Agregar %s') % ('Cita')
        return context

    def form_valid(self, form):
        """"Cita Crete View  form valid."""
        self.object = form.save(commit=True)

        msg = _(' %(name)s "%(obj)s" fue creado satisfactoriamente.') % {
            'name': capfirst(force_text(self.model._meta.verbose_name)),
            'obj': force_text(self.object)
        }

        messages.success(self.request, msg)
        log.warning(msg, extra=log_params(self.request))
        return super(CitaCreateView, self).form_valid(form)


class CitaUpdateView(UpdateView):
    """Cita Update View."""

    model = Cita
    form_class = CitaForm
    template_name = "cita/form.html"
    success_url = reverse_lazy("citas:cita_add")

    @method_decorator(permission_resource_required)
    def dispatch(self, request, *args, **kwargs):
        """Cita Create View dispatch."""
        key = self.kwargs.get(self.pk_url_kwarg, None)
        pk = SecurityKey.is_valid_key(request, key, 'doc_upd')
        if not pk:
            return HttpResponseRedirect(self.success_url)
        self.kwargs['pk'] = pk
        try:
            self.get_object()
        except Exception as e:
            messages.error(self.request, e)
            log.warning(force_text(e), extra=log_params(self.request))
            return HttpResponseRedirect(self.success_url)

        return super(CitaUpdateView,
                     self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """Cita Update View context data."""
        context = super(CitaUpdateView,
                        self).get_context_data(**kwargs)
        context['opts'] = self.model._meta
        # context['cmi'] = 'Cita'
        context['title'] = ('Actualizar %s') % ('Cita')
        return context

    def form_valid(self, form):
        """Cita Update View form_valid."""
        self.object = form.save(commit=False)

        self.object.usuario = self.request.user

        msg = ('%(name)s "%(obj)s" fue cambiado satisfacoriamente.') % {
            'name': capfirst(force_text(self.model._meta.verbose_name)),
            'obj': force_text(self.object)
        }
        if self.object.id:
            messages.success(self.request, msg)
            log.warning(msg, extra=log_params(self.request))
        return super(CitaUpdateView, self).form_valid(form)


class CitaDeleteView(DeleteView):
    """Cita Delete View."""

    model = Cita
    success_url = reverse_lazy('clivet:cita_list')

    @method_decorator(permission_resource_required)
    def dispatch(self, request, *args, **kwargs):
        """Cita Delete View dispatch."""
        key = self.kwargs['pk']
        pk = SecurityKey.is_valid_key(request, key, 'doc_del')
        if not pk:
            return HttpResponseRedirect(self.success_url)
        self.kwargs['pk'] = pk
        try:
            self.get_object()
        except Exception as e:
            messages.error(self.request, e)
            log.warning(force_text(e), extra=log_params(self.request))
            return HttpResponseRedirect(self.success_url)
        return super(CitaDeleteView,
                     self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        u"""
        Cita Delete View delte.

        Función para eliminar la Cita sobre un metodo que verifica las
        dependencias de que tiene la tabla mostrando un mensaje de validacion.
        """
        try:
            d = self.get_object()
            deps, msg = get_dep_objects(d)
            print(deps)
            if deps:
                messages.warning(
                    self.request,
                    ('No se puede Eliminar %(name)s') %
                    {
                        "name": capfirst(force_text(
                            self.model._meta.verbose_name)
                        ) + ' "' + force_text(d) + '"'
                    })
                raise Exception(msg)

            d.delete()
            msg = _(
                ' %(name)s "%(obj)s" fue eliminado satisfactorialmente.') % {
                'name': capfirst(force_text(self.model._meta.verbose_name)),
                'obj': force_text(d)
            }
            if not d.id:
                messages.success(self.request, msg)
                log.warning(msg, extra=log_params(self.request))
        except Exception as e:
            messages.error(request, e)
            log.warning(force_text(e), extra=log_params(self.request))
        return HttpResponseRedirect(self.success_url)

    def get(self, request, *args, **kwargs):
        """Cita Delete View get."""
        return self.delete(request, *args, **kwargs)


def GetCitaAjax(request):
    if request.is_ajax():
        try:
            citas = Cita.objects.all()
            results = []
            for cita in citas:
                cita_json = {}
                cita_json['id'] = cita.id
                cita_json['title'] = cita.evento.title
                cita_json['sin_atender'] = cita.estado
                cita_json['color'] = cita.evento.color
                cita_json['evento_id'] = cita.evento.id
                cita_json['descripcion'] = cita.descripcion
                cita_json['start'] = "%s" % cita.date
                cita_json['veterinario'] = cita.veterinario.id
                if cita.veterinario.person:
                    cita_json[
                        'veterinario_nombre'] = cita.veterinario.person.first_name
                    cita_json[
                        'veterinario_apellidos'] = cita.veterinario.person.last_name

                results.append(cita_json)
            data_json = json.dumps(results)
        except Exception as e:
            raise e

    else:
        data_json = 'fail'
    return HttpResponse(data_json, content_type='application/json')


def GetEventsAjax(request):
    if request.is_ajax():
        eventos = Evento.objects.all()
        data = serializers.serialize("json", eventos)
    else:
        data = 'fail'
    return HttpResponse(data, content_type='application/json')
