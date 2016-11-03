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
import json

from ..models.Venta import Venta
from ..forms.Venta import VentaForm
from ..models.Venta_Detalle import Detalle_Venta
from ..forms.VentaDetalle import Detalle_VentaForm
from django.db import transaction
import logging
log = logging.getLogger(__name__)


# def CrateVenta(request):

#     if request.method == "POST":
#         if 'form' in request.POST:
#             form = Detalle_VentaForm(request.POST)
#             if form.is_valid():
#                 Detalle_Venta.objects.create(
#                     producto=form.cleaned_data['producto'],
#                     venta=form.cleaned_data[
#                         'venta'],
#                     cantidad=form.cleaned_data[
#                         'cantidad'],
#                     igv=form.cleaned_data['igv'],
#                     importe=form.cleaned_data['importe'])
#                 # self.object = form1.save(commit=True)

#      #   if 'form1' in request.POST:
#                 form1 = VentaForm(request.POST)
#                 if form1.is_valid():
#                     Venta.objects.create(
#                         total=form1.cleaned_data[
#                             'total'],
#                         cliente=form1.cleaned_data['cliente'],
#                         trabajador=form1.cleaned_data['trabajador'])
#                     # <process form cleaned data>
#                     return HttpResponseRedirect('ventas/')

#     else:
#         #form1 = VentaForm()
#         form = Detalle_VentaForm()
#         # form1 = Detalle_VentaForm(initial={'cliente': 'rusbel'})

#     return render(request, 'ventas/index.html',
#                   {'form': form})


class MainCreateView(CreateView):
    u"""Tipo Documento Identidad."""

    model = Venta
    form_class = VentaForm
    template_name = "ventas/index.html"
    success_url = reverse_lazy("ventas:ventaslist",)

    @method_decorator(permission_resource_required)
    def dispatch(self, request, *args, **kwargs):
        """dispatch."""
        return super(MainCreateView,
                     self).dispatch(request, *args, **kwargs)

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
        self.object = form.save(commit=False)
        sid = transaction.savepoint()
        try:
            venta = json.loads(self.request.POST.get('data_venta'))
            print("______________1_________________")
            print(venta)
            print(self.request.POST.get('cliente'))
            self.object.total = venta['total']
            self.object.save()
            for p in venta['productos']:
                dv = Detalle_Venta(
                    producto_id=p['id'],
                    venta=self.object,
                    cantidad=p['cantidad'],
                    igv=p['igv'],
                    importe=p['importe'],
                )
                dv.save()

            # crearFactura.save()
            # print ("Factura guardado")
            # print (crearFactura.id)
            # for k in proceso['producto']:
            #     producto = Producto.objects.get(id=k['serial'])
            #     crearDetalle = DetalleFactura(
            #         producto=producto,
            #         descripcion=producto.nombre,
            #         precio=producto.precio,
            #         cantidad=int(k['cantidad']),
            #         impuesto=producto.igv * int(k['cantidad']),
            #         subtotal=producto.precio * int(k['cantidad']),
            #         factura=crearFactura
            #     )
            #     crearDetalle.save()

            # messages.success(
            #     self.request, 'La venta se ha realizado satisfactoriamente')
        except Exception as e:
            try:
                transaction.savepoint_rollback(sid)
            except:
                pass
            messages.error(self.request, e)

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

# @transaction.atomic
# def facturaCrear(request):

#     form = None
#     if request.method == 'POST':
#         sid = transaction.savepoint()
#         try:
#             proceso = json.loads(request.POST.get('proceso'))
#             print proceso
#             if 'serie' not in proceso:
#                 msg = 'Ingrese serie'
#                 raise Exception(msg)

#             if 'numero' not in proceso:
#                 msg = 'Ingrese numero'
#                 raise Exception(msg)

#             if 'clienProv' not in proceso:
#                 msg = 'El cliente no ha sido seleccionado'
#                 raise Exception(msg)

#             if len(proceso['producto']) <= 0:
#                 msg = 'No se ha seleccionado ningun producto'
#                 raise Exception(msg)

#             total = 0

#             for k in proceso['producto']:
#                 producto = Producto.objects.get(id=k['serial'])
#                 subTotal = (producto.precio) * int(k['cantidad'])
#                 total += subTotal

#             crearFactura = Factura(
#                 serie=proceso['serie'],
#                 numero=proceso['numero'],

#                 cliente=Cliente.objects.get(id=proceso['clienProv']),
#                 fecha=timezone.now(),
#                 total=total,
#                 vendedor=request.user
#             )
#             crearFactura.save()
#             print "Factura guardado"
#             print crearFactura.id
#             for k in proceso['producto']:
#                 producto = Producto.objects.get(id=k['serial'])
#                 crearDetalle = DetalleFactura(
#                     producto=producto,
#                     descripcion=producto.nombre,
#                     precio = producto.precio,
#                     cantidad=int(k['cantidad']),
#                     impuesto=producto.igv* int(k['cantidad']),
#                     subtotal=producto.precio * int(k['cantidad']),
#                     factura = crearFactura
#                 )
#                 crearDetalle.save()

#             messages.success(
#                 request, 'La venta se ha realizado satisfactoriamente')
#         except Exception, e:
#             try:
#                 transaction.savepoint_rollback(sid)
#             except:
#                 pass
#             messages.error(request, e)

# return render_to_response('facturacion/crear_factura.html', {'form':
# form}, context_instance=RequestContext(request))
