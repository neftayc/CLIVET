from django.conf.urls import url
from apps.compras.views.compras import compras
from apps.compras.views.Proveedor import (ProveedorListView, ProveedorCreateView, ProveedorUpdateView, ProveedorDeleteView)

urlpatterns = [
    # Examples
    url(r'compras', compras, name='compras'),

    url(r'^proveedor/listar/$', ProveedorListView.as_view(),  name="proveedor_list"),
    url(r'^proveedor/crear/$', ProveedorCreateView.as_view(),name="proveedor_add"),
    url(r'^proveedor/actualizar/(?P<pk>.*)/$', ProveedorUpdateView.as_view(), name="proveedor_upd"),
    url(r'^proveedor/eliminar/(?P<pk>.*)/$', ProveedorDeleteView.as_view(), name="proveedor_del"),
]
