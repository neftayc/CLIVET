from apps.utils.decorators import permission_resource_required
from apps.utils.forms import empty
from apps.utils.security import get_dep_objects, log_params, SecurityKey
from django.views import generic
from django.db import transaction

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

from ..forms.historiaform import HistoriaForm, MascotaHistoriDetailForm, HistoriaMascotaForm

from ..models.historia import Historial
from ..models.mascota import Mascota
from apps.clivet.models.cliente import Cliente

import logging
log = logging.getLogger(__name__)

# Create your views here.
class HistoriaListView(ListView):
    u"""Tipo Documento Identidad."""

    model = Historial
    paginate_by = settings.PER_PAGE
    template_name = "clinica/historia.html"

    @method_decorator(permission_resource_required)
    def dispatch(self, request, *args, **kwargs):
        """dispatch."""
        return super(HistoriaListView,
                     self).dispatch(request, *args, **kwargs)

    def get_paginate_by(self, queryset):
        """Paginate."""
        if 'all' in self.request.GET:
            return None
        return ListView.get_paginate_by(self, queryset)

    def get_queryset(self):
        """Tipo Doc List Queryset."""
        self.o = empty(self.request, 'o', '-id')
        self.f = empty(self.request, 'f', 'num_historia')
        self.q = empty(self.request, 'q', '')
        column_contains = u'%s__%s' % (self.f, 'contains')

        return self.model.objects.filter(
            **{column_contains: self.q}).order_by(self.o)

    def get_context_data(self, **kwargs):
        """
        Tipo Documento Identidad ListView List get context.
        Funcion con los primeros datos iniciales para la carga del template.
        """
        context = super(HistoriaListView,
                        self).get_context_data(**kwargs)
        context['opts'] = self.model._meta
        # context['cmi'] = 'menu' #  Validacion de manual del menu
        context['title'] = ('Seleccione %s para cambiar'
                            ) % capfirst('Tipo Documento')

        context['o'] = self.o
        context['f'] = self.f
        context['q'] = self.q.replace('/', '-')

        return context

class HistoriaCreateView(CreateView):
    """Tipo Documento Identidad."""

    model = Historial
    form_class = HistoriaForm
    template_name = "clinica/form/historia.html"
    success_url = reverse_lazy("clinica:listar_historia")

    @method_decorator(permission_resource_required)
    def dispatch(self, request, *args, **kwargs):
        """dispatch."""
        return super(HistoriaCreateView,
                     self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HistoriaCreateView,
                        self).get_context_data(**kwargs)
        context['opts'] = self.model._meta
        # context['cmi'] = 'tipodoc'
        context['title'] = ('Registro %s') % ('de historias clinicas')
        context['subtitle'] = ('Registrando %s') % ('nueva historia')
        return context

    def form_valid(self, form):
        """"Empresa Crete View  form valid."""
        self.object = form.save(commit=True)

        msg = _(' %(name)s "%(obj)s" fue creado satisfactoriamente.') % {
            'name': capfirst(force_text(self.model._meta.verbose_name)),
            'obj': force_text(self.object)
        }

        messages.success(self.request, msg)
        log.warning(msg, extra=log_params(self.request))
        return super(HistoriaCreateView, self).form_valid(form)


class HistoriaUpdateView(UpdateView):
    """Tipo Documento Update View."""

    model = Historial
    form_class = HistoriaForm
    template_name = "clinica/model.html"
    success_url = reverse_lazy("clinica:listar_historia")

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

        return super(HistoriaUpdateView,
                     self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """Tipo Documento Update View context data."""
        context = super(HistoriaUpdateView,
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
        return super(HistoriaUpdateView, self).form_valid(form)


class HistoriaDeleteView(DeleteView):
    """Empresa Delete View."""

    model = Historial
    success_url = reverse_lazy('clinica:listar_historia')

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
        return super(HistoriaDeleteView,
                     self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Empresa Delete View delte.
        Función para eliminar la empresa sobre un metodo que verifica las
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



class HistoriaMascotaCreateView(CreateView):
    """  """
    model = Historial
    form_class = HistoriaMascotaForm
    template_name = "clinica/form/historia.html"
    success_url = reverse_lazy("clinica:listar_historia")

    @method_decorator(permission_resource_required)
    def dispatch(self, request, *args, **kwargs):
        key = self.kwargs.get('pk', None)
        self.mascota_pk = None
        if key:
            self.mascota_pk = SecurityKey.is_valid_key(
                self.request, key, 'historia_cre')
            if not self.mascota_pk:
                return HttpResponseRedirect(reverse_lazy('sad:user-person_search'))
        return super(HistoriaMascotaCreateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HistoriaMascotaCreateView, self).get_context_data(**kwargs)
        context['opts'] = self.model._meta
        context['cmi'] = 'historia'
        context['title'] = _('Add %s') % capfirst(_('historia'))
        return context

    def get_form_kwargs(self):
        kwargs = super(HistoriaMascotaCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_initial(self):
        initial = super(HistoriaMascotaCreateView, self).get_initial()
        initial = initial.copy()
        if self.mascota_pk:
            d = Mascota.objects.get(pk=self.mascota_pk)
            if d:
                initial['nombre'] = d.nombre
                initial['dueño'] = d.dueño.persona
                initial['fecha_nacimiento'] = d.fecha_nacimiento
                initial['genero'] = d.genero
                initial['especie'] = d.especie
                initial['raza'] = d.raza
                initial['color'] = d.color
                initial['cond_corporal'] = d.cond_corporal
                initial['esterelizado'] = d.esterelizado
                initial['historia'] = d.historia
                initial['is_active'] = d.is_active
                initial['is_actived'] = d.is_actived
                initial['descripcion'] = d.descripcion
                initial['person_id'] = d.pk
        return initial

    @transaction.atomic
    def form_valid(self, form):
        sid = transaction.savepoint()
        try:
            try:
                mascota = Mascota.objects.get(
                    pk=self.request.POST.get("person_id"))
            except Exception as e:
                mascota = Mascota()
                mascota.save()
                pass
            mascota.nombre = form.cleaned_data['nombre']
            mascota.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            mascota.genero = form.cleaned_data['genero']
            mascota.especie = form.cleaned_data['especie']
            mascota.raza = form.cleaned_data['raza']
            mascota.color = form.cleaned_data['color']
            mascota.cond_corporal = form.cleaned_data['cond_corporal']
            mascota.esterelizado = form.cleaned_data['esterelizado']
            mascota.historia = form.cleaned_data['historia']
            mascota.is_active = form.cleaned_data['is_active']
            mascota.is_actived = form.cleaned_data['is_actived']
            mascota.descripcion = form.cleaned_data['descripcion']

            mascota.save()
            self.object = form.save(commit=False)
            self.object.mascota = mascota
            self.object.save()

            msg = _('The %(name)s "%(obj)s" was added successfully.') % {
                'name': capfirst(force_text(self.model._meta.verbose_name)),
                'obj': force_text(self.object)
            }
            if self.object.id:
                messages.success(self.request, msg)
                log.warning(msg, extra=log_params(self.request))
            return super(HistoriaMascotaCreateView, self).form_valid(form)
        except Exception as e:
            try:
                transaction.savepoint_rollback(sid)
            except:
                pass
            messages.success(self.request, e)
            log.warning(force_text(e), extra=log_params(self.request))
            return super(HistoriaMascotaCreateView, self).form_invalid(form)



class HistoriaMascotaDetailView(generic.DetailView):
    model = Historial
    success_url = reverse_lazy('clinica:listar_historia')

    @method_decorator(permission_resource_required)
    def dispatch(self, request, *args, **kwargs):
        key = self.kwargs.get(self.pk_url_kwarg, None)
        pk = SecurityKey.is_valid_key(request, key, 'historia_det')
        if not pk:
            return HttpResponseRedirect(self.success_url)
        self.kwargs['pk'] = pk
        try:
            self.get_object()
        except Exception as e:
            messages.error(self.request, e)
            log.warning(force_text(e), extra=log_params(self.request))
            return HttpResponseRedirect(self.success_url)

        return super(HistoriaMascotaDetailView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HistoriaMascotaDetailView, self).get_context_data(**kwargs)
        context['opts'] = self.model._meta
        context['cmi'] = 'historia'
        context['title'] = _('Detail %s') % capfirst(_('historia'))

        #context['object'] = self.object

        if self.object.mascota:
            initial = {
                'num_historia': self.object.num_historia,
                'created_ath': self.object.created_ath,
                'veterinario': self.object.veterinario,
                'nombre': self.object.mascota.nombre,
                'dueño': self.object.mascota.dueño.persona,
                'direccion': self.object.mascota.dueño.direccion,
                'ciudad': self.object.mascota.dueño.ciudad,
                'telefono': self.object.mascota.dueño.telefono,
                'edad': self.object.mascota.fecha_nacimiento,
                'genero': self.object.mascota.genero,
                'especie': self.object.mascota.especie,
                'raza': self.object.mascota.raza,
                'color': self.object.mascota.color,
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
        context['form'] = MascotaHistoriDetailForm(initial=initial)
        return context
