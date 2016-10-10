from django.conf.urls import url
from apps.ventas.views.main import Ventas
from apps.ventas.views.Departamento import *


urlpatterns = [
    # Examples
    url(r'ventas', Ventas.as_view()),
    url(r'^departamento/listar/$', DepartamentoListView.as_view(),
        name = "departamento_list"),
    url(r'^departamento/crear/$', DepartamentoCreateView.as_view(),
        name="departamento_add"),
    url(r'^departamento/actualizar/(?P<pk>.*)/$', DepartamentoUpdateView.as_view(),
        name="departamento_upd"),
    url(r'^departamento/eliminar/(?P<pk>.*)/$', DepartamentoDeleteView.as_view(),
        name="departamento_del"),

]
