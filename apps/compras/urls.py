from django.conf.urls import url
from django.views.generic.base import TemplateView
from apps.compras.views.proveedor import proveedor
from apps.compras.views.compras import compras

urlpatterns = [
    # Examples
    url(r'compras', compras,name='compras'),
    url(r'proveedor', proveedor, name='proveedor'),
]
