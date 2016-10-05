u"""Url Conf."""

from apps.conf.views.TipoDocumentoIdentidad import (
    TipoDocumentoIdentidadListView, TipoDocumentoIdentidadCreateView, TipoDocumentoIdentidadUpdateView,
    TipoDocumentoIdentidadDeleteView
)

from django.conf.urls import url

urlpatterns = [

    url(r'^tipo_documento/listar/$', TipoDocumentoIdentidadListView.as_view(),
        name="tipo_documento_list"),
    url(r'^tipo_documento/crear/$', TipoDocumentoIdentidadCreateView.as_view(),
        name="tipo_documento_add"),
    url(r'^tipo_documento/actualizar/(?P<pk>.*)/$', TipoDocumentoIdentidadUpdateView.as_view(),
        name="tipo_documento_upd"),
    url(r'^tipo_documento/eliminar/(?P<pk>.*)/$', TipoDocumentoIdentidadDeleteView.as_view(),
        name="tipo_documento_del"),
]
