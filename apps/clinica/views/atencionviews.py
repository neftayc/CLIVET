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

from ..forms.atencionform import AtencionForm, AtencionMascotaDetailForm
from ..models.atencion import Atencion
from ..models.colamedica import ColaMedica
from ..models.mascota import Mascota
import logging
log = logging.getLogger(__name__)

class AtencionListView(ListView):
    model = Atencion
    template_name = "clinica/atencion.html"

    def get_context_data(self, **kwargs):
        #mascota = Mascota.objects.get(nombre='Boby')
        context = super(AtencionListView, self).get_context_data(**kwargs)
        mascota = Mascota.objects.get(id=self.kwargs['pk'])
        context['opts'] = self.model._meta
        context['atencion'] = Atencion.objects.filter(colamedica__historia__mascota__nombre=mascota ).order_by('pk')
        context['nombre'] = mascota
        context['dueño'] = mascota.dueño
        context['raza'] = mascota.raza
        context['fecha'] = mascota.fecha_nacimiento
        context['especie'] = mascota.especie
        context['genero'] = mascota.genero
        context['esterelizado'] = mascota.esterelizado
        context['peso'] = '20kg'
        context['color'] = mascota.color
        context['cantidad'] = context['atencion'].count()

        if mascota:
            initial = {
                'nombre': mascota.nombre,
                'dueño': mascota.dueño.persona,
                'edad': mascota.fecha_nacimiento,
                'genero': mascota.genero,
                'especie': mascota.especie,
                'raza': mascota.raza,
                'color': mascota.color,
            }
        context['form'] = AtencionMascotaDetailForm(initial=initial)
        return context

class AtencionCreateView(CreateView):
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
                return HttpResponseRedirect(reverse_lazy('clinica: listar_medica'))
        return super(AtencionCreateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AtencionCreateView, self).get_context_data(**kwargs)
        context['opts'] = self.model._meta
        #context['cmi'] = 'atencion'
        context['nombre'] = self.medica_pk
        context['title'] = _('%s') % capfirst(_('atencion'))
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
                initial['nombre'] = d.historia.mascota.nombre
                initial['raza'] = d.historia.mascota.raza
                initial['dueño'] = d.historia.mascota.dueño
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
                colamedica = ColaMedica.objects.get(pk=self.request.POST.get("person_id"))
            except Exception as e:
                colamedica = ColaMedica()
                colamedica.save()

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
