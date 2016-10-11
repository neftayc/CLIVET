from django.conf.urls import url
from apps.clivet.views.main import clivet
from .views.trabajador import (
    TrabajadorListView, TrabajadorCreateView, TrabajadorUpdateView,
    TrabajadorDeleteView
)
from .views.cliente import (
    ClienteListView, ClienteCreateView, ClienteUpdateView,
    ClienteDeleteView
)
from .views.persona import (
    PersonaListView, PersonaCreateView, PersonaUpdateView,
    PersonaDeleteView
)

urlpatterns = [
    url(r'^clivet', clivet, name='clivet'),
    # ===================TRABAJADOR==========================
    url(r'^trabajador/listar/$', TrabajadorListView.as_view(),
        name="trabajador_list"),
    url(r'^trabajador/crear/$', TrabajadorCreateView.as_view(),
        name="trabajador_add"),
    url(r'^trabajador/actualizar/(?P<pk>.*)/$', TrabajadorUpdateView.as_view(),
        name="trabajador_upd"),
    url(r'^trabajador/eliminar/(?P<pk>.*)/$', TrabajadorDeleteView.as_view(),
        name="trabajador_del"),
    # ===================CLIENTE==========================
    url(r'^cliente/listar/$', ClienteListView.as_view(),
        name="cliente_list"),
    url(r'^cliente/crear/$', ClienteCreateView.as_view(),
        name="cliente_add"),
    url(r'^cliente/actualizar/(?P<pk>.*)/$', ClienteUpdateView.as_view(),
        name="cliente_upd"),
    url(r'^cliente/eliminar/(?P<pk>.*)/$', ClienteDeleteView.as_view(),
        name="cliente_del"),
    # ===================CLIENTE==========================
    url(r'^persona/listar/$', PersonaListView.as_view(),
        name="persona_list"),
    url(r'^persona/crear/$', PersonaCreateView.as_view(),
        name="persona_add"),
    url(r'^persona/actualizar/(?P<pk>.*)/$', PersonaUpdateView.as_view(),
        name="persona_upd"),
    url(r'^persona/eliminar/(?P<pk>.*)/$', PersonaDeleteView.as_view(),
        name="persona_del"),
]
