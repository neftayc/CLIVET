from django.conf.urls import url
from apps.ventas.views.main import Ventas
from apps.ventas.views.Departamento import *
from apps.ventas.views.Categoria import *
from apps.ventas.views.Producto import *
from apps.ventas.views.UnidadMedida import *


urlpatterns = [
    url(r'ventas', Ventas.as_view()),
    # departamento
    url(r'^departamento/listar/$', DepartamentoListView.as_view(),
        name="departamento_list"),
    url(r'^departamento/crear/$', DepartamentoCreateView.as_view(),
        name="departamento_add"),
    url(r'^departamento/actualizar/(?P<pk>.*)/$', DepartamentoUpdateView.as_view(),
        name="departamento_upd"),
    url(r'^departamento/eliminar/(?P<pk>.*)/$', DepartamentoDeleteView.as_view(),
        name="departamento_del"),
    # categoria
    url(r'^categoria/listar/$', CategoriaListView.as_view(),
        name="categoria_list"),
    url(r'^categoria/crear/$', CategoriaCreateView.as_view(),
        name="categoria_add"),
    url(r'^categoria/actualizar/(?P<pk>.*)/$', CategoriaUpdateView.as_view(),
        name="categoria_upd"),
    url(r'^categoria/eliminar/(?P<pk>.*)/$', CategoriaDeleteView.as_view(),
        name="categoria_del"),
    # categoria
    url(r'^producto/listar/$', ProductoListView.as_view(),
        name="producto_list"),
    url(r'^producto/crear/$', ProductoCreateView.as_view(),
        name="producto_add"),
    url(r'^producto/actualizar/(?P<pk>.*)/$', ProductoUpdateView.as_view(),
        name="producto_upd"),
    url(r'^producto/eliminar/(?P<pk>.*)/$', ProductoDeleteView.as_view(),
        name="producto_del"),
    # categoria
    url(r'^uni/listar/$', UnidadMedidaListView.as_view(),
        name="unidad_medida_list"),
    url(r'^uni/crear/$', UnidadMedidaCreateView.as_view(),
        name="unidad_medida_add"),
    url(r'^uni/actualizar/(?P<pk>.*)/$', UnidadMedidaUpdateView.as_view(),
        name="unidad_medida_upd"),
    url(r'^uni/eliminar/(?P<pk>.*)/$', UnidadMedidaDeleteView.as_view(),
        name="unidad_medida_del"),
]
