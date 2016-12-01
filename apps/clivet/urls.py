from django.conf.urls import url
from apps.clivet.views.main import clivet
from .views.cliente import *
from .views.trabajador import *

urlpatterns = [
    url(r'^clivet', clivet, name='clivet'),
    # ===================CLIENTE==========================
    url(r'^cliente/listar/$', ClienteListView.as_view(),
        name="cliente_list"),
    url(r'^cliente/crear/$', ClienteCreateView.as_view(),
        name="cliente_add"),
    url(r'^cliente/actualizar/(?P<pk>.*)/$', ClienteUpdateView.as_view(),
        name="cliente_upd"),
    url(r'^cliente/eliminar/(?P<pk>.*)/$', ClienteDeleteView.as_view(),
        name="cliente_del"),
    url(r'^cliente/crear/ajax$', PostClienteAjax,
        name="post_cliente_ajax"),
    # ===================TRABAJADOR==========================
    # url(r'^trabajador/listar/$', TrabajadorListView.as_view(),
    #     name="trabajador_list"),
    # url(r'^trabajador/crear/$', TrabajadorCreateView.as_view(),
    #     name="trabajador_add"),
    url(r'^perfil/editar/$', TrabajadorUpdateView.as_view(),
        name="trabajador_upd"),
    # url(r'^trabajador/eliminar/(?P<pk>.*)/$', TrabajadorDeleteView.as_view(),
    #     name="trabajador_del"),
]
