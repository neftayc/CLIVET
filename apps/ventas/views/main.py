u"""Módulo View Venta"""

from apps.utils.decorators import permission_resource_required
from apps.utils.forms import empty
from apps.utils.security import get_dep_objects, log_params, SecurityKey

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
from django.shortcuts import render

from ..models.Venta import Venta
from ..forms.Venta import VentaForm
from ..models.Venta_Detalle import Detalle_Venta
from ..forms.VentaDetalle import Detalle_VentaForm

import logging
log = logging.getLogger(__name__)


class MainCreateView(CreateView):
    u"""Tipo Documento Identidad."""

    model = Venta, Detalle_Venta
    form_class = VentaForm, Detalle_VentaForm
    template_name = "ventas/index.html"
    success_url = reverse_lazy("ventas:ventaslist",)

    @method_decorator(permission_resource_required)
    def dispatch(self, request, *args, **kwargs):
        """dispatch."""
        if request.method == "POST":
            form = VentaForm(request.POST)
            if form.is_valid():
                # <process form cleaned data>
                return HttpResponseRedirect('ventas/index.html')
        elif request.method == "POST":
            form1 = Detalle_VentaForm(request.POST)
            if form1.is_valid():
                # <process form cleaned data>
                return HttpResponseRedirect('ventas/index.html')
        else:
            form = VentaForm()
            form1 = Detalle_VentaForm(initial={'cliente': 'rusbel'})

        return render(request, 'ventas/index.html', {'l': form, 's': form1})

    def get_context_data(self, **kwargs):
        """
        Tipo Documento Identidad ListView List get context.

        Funcion con los primeros datos iniciales para la carga del template.
        """
        context = super(MainCreateView,
                        self).get_context_data(**kwargs)
        context['opts'] = self.model._meta
        # context['cmi'] = 'tipodoc'
        context['title'] = ('Agregar %s') % ('Venta')
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
        return super(MainCreateView, self).form_valid(form)


class DetalleVentaCreateView(CreateView):
    u"""Tipo Documento Identidad."""

    model = Detalle_Venta
    form_class = Detalle_VentaForm
    template_name = "ventas/index.html"
    success_url = reverse_lazy("ventas:recepcion_list")

    @method_decorator(permission_resource_required)
    def dispatch(self, request, *args, **kwargs):
        """dispatch."""
        return super(DetalleVentaCreateView,
                     self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Tipo Documento Identidad ListView List get context.

        Funcion con los primeros datos iniciales para la carga del template.
        """
        context = super(DetalleVentaCreateView,
                        self).get_context_data(**kwargs)
        context['opts'] = self.model._meta
        # context['cmi'] = 'tipodoc'
        context['title'] = ('Agregar %s') % ('DetalleVenta')
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
        return super(DetalleVentaCreateView, self).form_valid(form)
