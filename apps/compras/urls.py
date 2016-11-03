from django.conf.urls import url
#from apps.compras.views.compras import compras
from apps.compras.views.Proveedor import (ProveedorListView, ProveedorCreateView, ProveedorUpdateView, ProveedorDeleteView)
from apps.compras.views.compra import (CompraListView, CompraCreateView, CompraUpdateView)
urlpatterns = [
    # Examples
    #url(r'compras', compras,name='compras'),

    #Proveedor
    url(r'^proveedor/listar/$', ProveedorListView.as_view(),  name="proveedor_list"),
    url(r'^proveedor/crear/$', ProveedorCreateView.as_view(),name="proveedor_add"),
    url(r'^proveedor/actualizar/(?P<pk>.*)/$', ProveedorUpdateView.as_view(), name="proveedor_upd"),
    url(r'^proveedor/eliminar/(?P<pk>.*)/$', ProveedorDeleteView.as_view(), name="proveedor_del"),

    #Compra
    url(r'^compra/listar/$', CompraListView.as_view(),  name="compra_list"),
    url(r'^compra/crear/$', CompraCreateView.as_view(),name="compra_add"),
    url(r'^compra/actualizar/(?P<pk>.*)/$', CompraUpdateView.as_view(), name="compra_upd"),
    #url(r'^compra/eliminar/(?P<pk>.*)/$', CompraDeleteView.as_view(), name="compra_del"),
    
]
