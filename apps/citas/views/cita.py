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


def CitaAjax(request):
    if request.is_ajax():
        data = serializers.serialize(
            "json", Cita.objects.all())
        return HttpResponse(data, content_type='application/json')


class CitaCreateView(CreateView):
    u"""Cita."""

    model = Cita
    form_class = CitaForm
    template_name = "cita/form.html"
    success_url = reverse_lazy("clivet:cita_list")

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
    success_url = reverse_lazy("clivet:cita_list")

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
