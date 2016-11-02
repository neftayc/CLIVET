from apps.utils.decorators import permission_resource_required
from apps.utils.forms import empty
from apps.utils.security import get_dep_objects, log_params, SecurityKey
from django.views import generic
from django.db import transaction

from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.utils.encoding import force_text
from django.utils.text import capfirst
from django.utils.translation import ugettext as _
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView

from ..forms.atencionform import AtencionForm, AtencionMascotaForm

from ..models.atencion import Atencion
from ..models.colamedica import ColaMedica
from ..models.mascota import Mascota
import logging
log = logging.getLogger(__name__)

# Create your views here.
class AtencionListView(ListView):
    u"""Tipo Documento Identidad."""

    model = Atencion
    template_name = "clinica/atencion.html"

    def get_context_data(self, **kwargs):

        mascota = Mascota.objects.get(nombre='Boby')
        context = super(AtencionListView, self).get_context_data(**kwargs)
        context['atencion'] = Atencion.objects.filter(colamedica__historia__mascota__nombre=mascota ).order_by('pk')
        context['cantidad'] = context['atencion'].count()
        return context


class AtencionCreateView(CreateView):
    """Tipo Documento Identidad."""
    model = Atencion
    form_class = AtencionForm
    template_name = "clinica/form/atencion.html"
    success_url = reverse_lazy("clinica:listar_medica")

    @method_decorator(permission_resource_required)
    def dispatch(self, request, *args, **kwargs):
        """dispatch."""
        key = self.kwargs.get('pk', None)
        self.medica_pk = None
        if key:
            self.medica_pk = SecurityKey.is_valid_key(
                self.request, key, 'medica_cre')
            if not self.medica_pk:
                return HttpResponseRedirect(reverse_lazy('sad:user-person_search'))
        return super(AtencionCreateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AtencionCreateView, self).get_context_data(**kwargs)
        context['opts'] = self.model._meta
        context['cmi'] = 'atencion'
        context['title'] = _('Add %s') % capfirst(_('atencion'))
        return context

    def get_form_kwargs(self):
        kwargs = super(AtencionCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_initial(self):
        initial = super(AtencionCreateView, self).get_initial()
        initial = initial.copy()
        if self.medica_pk:
            d = ColaMedica.objects.get(pk=self.medica_pk)
            if d:
                initial['historia'] = d.historia.num_historia
                initial['descripcion'] = d.descripcion
                initial['estado'] = d.estado
                initial['person_id'] = d.pk
        return initial

    @transaction.atomic
    def form_valid(self, form):
        sid = transaction.savepoint()
        try:
            try:
                colamedica = ColaMedica.objects.get(
                    pk=self.request.POST.get("person_id"))
            except Exception as e:
                colamedica = ColaMedica()
                colamedica.save()
            colamedica.descripcion = form.cleaned_data['descripcion']
            colamedica.estado = form.cleaned_data['estado']

            colamedica.save()
            self.object = form.save(commit=False)
            self.object.colamedica = colamedica
            self.object.save()

            msg = _('The %(name)s "%(obj)s" was added successfully.') % {
                'name': capfirst(force_text(self.model._meta.verbose_name)),
                'obj': force_text(self.object)
            }
            if self.object.id:
                messages.success(self.request, msg)
                log.warning(msg, extra=log_params(self.request))
            return super(AtencionCreateView, self).form_valid(form)
        except Exception as e:
            try:
                transaction.savepoint_rollback(sid)
            except:
                pass
            messages.success(self.request, e)
            log.warning(force_text(e), extra=log_params(self.request))
            return super(AtencionCreateView, self).form_invalid(form)


class AtencionUpdateView(UpdateView):
    """Tipo Documento Update View."""

    model = Atencion
    form_class = AtencionForm
    template_name = "clinica/model.html"
    success_url = reverse_lazy("clinica:listar_atencion")

    @method_decorator(permission_resource_required)
    def dispatch(self, request, *args, **kwargs):
        """Tipo Documento Create View dispatch."""
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

        return super(AtencionUpdateView,
                     self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """Tipo Documento Update View context data."""
        context = super(AtencionUpdateView,
                        self).get_context_data(**kwargs)
        context['opts'] = self.model._meta
        # context['cmi'] = 'empresa'
        context['title'] = ('Actualizar %s') % ('Tipo Documento')
        return context

    def form_valid(self, form):
        """Tipo Documento Update View form_valid."""
        self.object = form.save(commit=False)

        self.object.usuario = self.request.user

        msg = ('%(name)s "%(obj)s" fue cambiado satisfacoriamente.') % {
            'name': capfirst(force_text(self.model._meta.verbose_name)),
            'obj': force_text(self.object)
        }
        if self.object.id:
            messages.success(self.request, msg)
            log.warning(msg, extra=log_params(self.request))
        return super(AtencionUpdateView, self).form_valid(form)


class AtencionDeleteView(DeleteView):
    """Empresa Delete View."""

    model = Atencion
    success_url = reverse_lazy('clinica:listar_atencion')

    @method_decorator(permission_resource_required)
    def dispatch(self, request, *args, **kwargs):
        """Empresa Delete View dispatch."""
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
        return super(AtencionDeleteView,
                     self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
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
                ' %(name)s "%(obj)s" fuel eliminado satisfactorialmente.') % {
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
        """Empresa Delete View get."""
        return self.delete(request, *args, **kwargs)


class AtencionMedicaView(generic.DetailView):
    model = ColaMedica
    success_url = reverse_lazy('clinica:listar_medica')

    @method_decorator(permission_resource_required)
    def dispatch(self, request, *args, **kwargs):
        key = self.kwargs.get(self.pk_url_kwarg, None)
        pk = SecurityKey.is_valid_key(request, key, 'aten_det')
        if not pk:
            return HttpResponseRedirect(self.success_url)
        self.kwargs['pk'] = pk
        try:
            self.get_object()
        except Exception as e:
            messages.error(self.request, e)
            log.warning(force_text(e), extra=log_params(self.request))
            return HttpResponseRedirect(self.success_url)

        return super(AtencionMedicaView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AtencionMedicaView, self).get_context_data(**kwargs)
        context['opts'] = self.model._meta
        context['cmi'] = 'historia'
        context['title'] = _('Detail %s') % capfirst(_('historia'))

        #context['object'] = self.object

        if self.object.historia:
            initial = {
                'num_historia': self.object.historia.num_historia,
                'created_ath': self.object.historia.created_ath,
                'veterinario': self.object.historia.veterinario,
                'nombre': self.object.historia.mascota.nombre,
                'dueño': self.object.historia.mascota.dueño.persona,
                'direccion': self.object.historia.mascota.dueño.direccion,
                'ciudad': self.object.historia.mascota.dueño.ciudad,
                'telefono': self.object.historia.mascota.dueño.telefono,
                'edad': self.object.historia.mascota.fecha_nacimiento,
                'genero': self.object.historia.mascota.genero,
                'especie': self.object.historia.mascota.especie,
                'raza': self.object.historia.mascota.raza,
                'color': self.object.historia.mascota.color,
            }
        else:
            initial = {
                'username': self.object.username,
                'email': self.object.email,
                'is_superuser': self.object.is_superuser,
                'is_staff': self.object.is_staff,
                'is_active': self.object.is_active,
                'photo': '-',
                'first_name': '-',
                'last_name': '-',
                'identity_type': '-',
                'identity_num': '-',
                'hgroups': UserHeadquar.objects.filter(user=self.object).order_by('headquar'),
                'egroups': UserEnterprise.objects.filter(user=self.object).order_by('enterprise'),
                'agroups': UserAssociation.objects.filter(user=self.object).order_by('association'),
                'status': UserStatus.objects.filter(user=self.object).order_by('-created_at'),
            }
        context['form'] = AtencionMascotaForm(initial=initial)
        return context



class MainAtencionesView(TemplateView):

    template_name = 'clinica/atencion.html'

    def get_context_data(self, **kwargs):
        context = super(MainAtencionesView, self).get_context_data(**kwargs)
        context['title'] = _('Add %s') % capfirst(_('atencion'))
        context['atencion'] = Atencion.objects.filter(colamedica = '0001').order_by('anamnesis')
        context['cantidad'] = context['atencion'].count()
        return context
