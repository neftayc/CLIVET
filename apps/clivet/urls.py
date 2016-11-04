from django.conf.urls import url
from apps.clivet.views.main import clivet
from .views.cliente import (
    ClienteListView, ClienteCreateView, ClienteUpdateView,
    ClienteDeleteView
)

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
]
