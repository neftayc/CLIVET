from django.conf.urls import url
from .views.cita import (
    CitaView, CitaAjax, CitaCreateView, CitaUpdateView,
    CitaDeleteView
)

urlpatterns = [
    # ===================CLIENTE==========================
    url(r'^$', CitaView.as_view(),
        name="cita_list"),
    url(r'^listar/$', CitaAjax, name="cita_list_get"),
    url(r'^crear/$', CitaCreateView.as_view(),
        name="cita_add"),
    url(r'^actualizar/(?P<pk>.*)/$', CitaUpdateView.as_view(),
        name="cita_upd"),
    url(r'^eliminar/(?P<pk>.*)/$', CitaDeleteView.as_view(),
        name="cita_del"),
]
