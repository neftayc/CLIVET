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

from ..forms.historiaform import MascotaHistoriDetailForm, HistoriaMascotaForm

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
        context['title'] = ('Seleccione %s para mas detalle'
                            ) % capfirst(' una historia')

        context['o'] = self.o
        context['f'] = self.f
        context['q'] = self.q.replace('/', '-')

        return context

class HistoriaMascotaCreateView(CreateView):
    """  """
    model = Historial
    form_class = HistoriaMascotaForm
    template_name = "clinica/form/historia.html"
    success_url = reverse_lazy("clinica:crear_medica")

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
        context['datos']= Historial.objects.all()
        context['cantidad']=context['datos'].count()+1
        context['title'] = _('Add %s') % capfirst(_('historia'))
        context['subtitle'] = _('Registro de %s') % capfirst(_('historia clinica'))
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
                initial['dueño'] = d.dueño
                initial['fecha_nacimiento'] = d.fecha_nacimiento
                initial['historia'] = d.historia
                initial['caracter'] = d.caracter
                initial['actividad'] = d.actividad
                initial['habitar'] = d.habitar
                initial['alimentacion'] = d.alimentacion
                initial['aptitup'] = d.aptitup
                initial['convive'] = d.convive
                initial['person_id'] = d.pk
        return initial

    @transaction.atomic
    def form_valid(self, form):
        form.instance.veterinario = self.request.user
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
            mascota.dueño = form.cleaned_data['dueño']
            mascota.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            mascota.historia = form.cleaned_data['historia']
            mascota.caracter = form.cleaned_data['alimentacion']
            mascota.actividad = form.cleaned_data['caracter']
            mascota.habitar = form.cleaned_data['actividad']
            mascota.alimentacion = form.cleaned_data['habitar']
            mascota.Aptitup = form.cleaned_data['aptitup']
            mascota.convive = form.cleaned_data['convive']

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
