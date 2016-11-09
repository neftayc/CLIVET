from apps.utils.decorators import permission_resource_required
from apps.utils.forms import empty
from apps.utils.security import get_dep_objects, log_params, SecurityKey

from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.decorators import method_decorator
from django.utils.encoding import force_text
from django.utils.text import capfirst
from django.utils.translation import ugettext as _
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView

from apps.clivet.models.cliente import Cliente
from ..models.historia import Historial
from ..models.colamedica import ColaMedica
from ..forms.colamedicaform import ColaMedicaForm

import logging
log = logging.getLogger(__name__)



class BusquedaClientView(ListView):

    model = Cliente
    template_name = 'clinica/busqueda.html'
    context_object_name = 'clientes'

from django.core import serializers


class BusquedaClientAjaxView(TemplateView):

    def get(self, request, *args, **kwargs):
        id_cliente = request.GET['id']
        mascotas = Historial.objects.filter(mascota__dueño__id = id_cliente)
        data = serializers.serialize('json', mascotas, fields=('id', 'mascota','num_historia'))
        return HttpResponse(data, content_type='application/json')
