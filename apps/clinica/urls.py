from django.conf.urls import url


from .views.atencionviews import (AtencionListView, AtencionCreateView, AtencionUpdateView, AtencionDeleteView, AtencionMedicaView, MainAtencionesView)
from .views.colamedicaviews import (ColaMedicaListView, ColaMedicaCreateView, ColaMedicaUpdateView, ColaMedicaDeleteView, ColasMedicasListView)
from .views.consultaviews import (ConsultaListView, ConsultaCreateView, ConsultaUpdateView, ConsultaDeleteView, lista_doctores1)
from .views.historiaviews import (HistoriaListView, HistoriaCreateView, HistoriaUpdateView, HistoriaDeleteView, HistoriaMascotaDetailView, HistoriaMascotaCreateView)
from .views.mascotaviews import (MascotaListView, MascotaCreateView, MascotaUpdateView, MascotaUpdateActiveView)
from .views.notasviews import (NotasListView, NotasCreateView, NotasUpdateView, NotasDeleteView)
from .views.vacunacionviews import (BusquedaClientView, BusquedaClientAjaxView)

urlpatterns = [

    url(r'^cliente/busqueda/$', BusquedaClientView.as_view(), name="busqueda_client"),
    url(r'^cliente/busqueda_ajax/$', BusquedaClientAjaxView.as_view()),

    #Atencion
    url(r'^atencion/listar/(?P<pk>\d+)/$', AtencionListView.as_view(), name="listar_atencion"),

    url(r'^atencion/mainlistar/$', MainAtencionesView.as_view(), name="mainlistar"),

    url(r'^atencion/crear/(?P<pk>.*)/$', AtencionCreateView.as_view(), name="crear_atencion"),
    url(r'^atencion/actualizar/(?P<pk>.*)/$', AtencionUpdateView.as_view(), name="actualizar_atencion"),
    url(r'^atencion/eliminar/(?P<pk>.*)/$', AtencionDeleteView.as_view(), name="eliminar_atencion"),

    #Cola Medica
    url(r'^colamedica/listar/$', ColaMedicaListView.as_view(), name="listar_medica"),
    url(r'^colamedica/lista/$', ColasMedicasListView.as_view(), name="lista_medica"),
    url(r'^colamedica/crear/$', ColaMedicaCreateView.as_view(), name="crear_medica"),
    url(r'^colamedica/actualizar/(?P<pk>.*)/$', ColaMedicaUpdateView.as_view(), name="actualizar_medica"),
    url(r'^colamedica/eliminar/(?P<pk>.*)/$', ColaMedicaDeleteView.as_view(), name="eliminar_medica"),

    url(r'^colamedica/detail/(?P<pk>.*)/$', AtencionMedicaView.as_view(), name='colamedica_detail'),

    #CONSULTA
    url(r'^consulta/listar/$', ConsultaListView.as_view(), name="listar_consulta"),
    url(r'^consulta/crear/$', ConsultaCreateView.as_view(), name="crear_consulta"),
    url(r'^consulta/actualizar/(?P<pk>.*)/$', ConsultaUpdateView.as_view(), name="actualizar_consulta"),
    url(r'^consulta/eliminar/(?P<pk>.*)/$', ConsultaDeleteView.as_view(), name="eliminar_consulta"),
    url(r'^consulta/solo_url/$', lista_doctores1),
    #Historia
    url(r'^historia/listar/$', HistoriaListView.as_view(), name="listar_historia"),
    url(r'^historia/crear/$', HistoriaCreateView.as_view(), name="crear_historia"),
    url(r'^historia/mascota_add/(?P<pk>.*)/$', HistoriaMascotaCreateView.as_view(), name='crear_historiamascota'),

    url(r'^historia/actualizar/(?P<pk>.*)/$', HistoriaUpdateView.as_view(), name="actualizar_historia"),
    url(r'^historia/eliminar/(?P<pk>.*)/$', HistoriaDeleteView.as_view(), name="eliminar_historia"),
    url(r'^historia/detail/(?P<pk>.*)/$', HistoriaMascotaDetailView.as_view(), name='historia_detail'),

    # Mascota
    url(r'^mascota/listar/$', MascotaListView.as_view(), name="listar_mascotas"),
    url(r'^mascota/crear/$', MascotaCreateView.as_view(), name="crear_mascota"),
    url(r'^mascota/actualizar/(?P<pk>.*)/$', MascotaUpdateView.as_view(), name="actualizar_mascota"),
    url(r'^mascota/state/(?P<state>[\w\d\-]+)/(?P<pk>.*)/$',
        MascotaUpdateActiveView.as_view(), name='mascota-state'),

    #NOTAS
    url(r'^notas/listar/$', NotasListView.as_view(), name="listar_notas"),
    url(r'^notas/crear/$', NotasCreateView.as_view(), name="crear_notas"),
    url(r'^notas/actualizar/(?P<pk>.*)/$', NotasUpdateView.as_view(), name="actualizar_notas"),
    url(r'^notas/eliminar/(?P<pk>.*)/$', NotasDeleteView.as_view(), name="eliminar_notas"),

]
