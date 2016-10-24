from django.conf.urls import url

from .views.atencionviews import (AtencionListView, AtencionCreateView, AtencionUpdateView, AtencionDeleteView, AtencionMedicaView)
from .views.colamedicaviews import (ColaMedicaListView, ColaMedicaCreateView, ColaMedicaUpdateView, ColaMedicaDeleteView)
from .views.consultaviews import (ConsultaListView, ConsultaCreateView, ConsultaUpdateView, ConsultaDeleteView)
from .views.historiaviews import (HistoriaListView, HistoriaCreateView, HistoriaUpdateView, HistoriaDeleteView, HistoriaMascotaDetailView)
from .views.mascotaviews import (MascotaListView, MascotaCreateView, MascotaUpdateView, MascotaDeleteView, MascotaUpdateActiveView)
from .views.notasviews import (NotasListView, NotasCreateView, NotasUpdateView, NotasDeleteView)
from .views.vacunacionviews import (VacunacionListView, VacunacionCreateView, VacunacionUpdateView, VacunacionDeleteView)

urlpatterns = [
    #Atencion
    url(r'^atencion/listar/$', AtencionListView.as_view(), name="listar_atencion"),
    url(r'^atencion/crear/$', AtencionCreateView.as_view(), name="crear_atencion"),
    url(r'^atencion/actualizar/(?P<pk>.*)/$', AtencionUpdateView.as_view(), name="actualizar_atencion"),
    url(r'^atencion/eliminar/(?P<pk>.*)/$', AtencionDeleteView.as_view(), name="eliminar_atencion"),

    #Cola Medica
    url(r'^colamedica/listar/$', ColaMedicaListView.as_view(), name="listar_medica"),
    url(r'^colamedica/crear/$', ColaMedicaCreateView.as_view(), name="crear_medica"),
    url(r'^colamedica/actualizar/(?P<pk>.*)/$', ColaMedicaUpdateView.as_view(), name="actualizar_medica"),
    url(r'^colamedica/eliminar/(?P<pk>.*)/$', ColaMedicaDeleteView.as_view(), name="eliminar_medica"),

    url(r'^colamedica/detail/(?P<pk>.*)/$', AtencionMedicaView.as_view(), name='colamedica_detail'),

    #CONSULTA
    url(r'^consulta/listar/$', ConsultaListView.as_view(), name="listar_consulta"),
    url(r'^consulta/crear/$', ConsultaCreateView.as_view(), name="crear_consulta"),
    url(r'^consulta/actualizar/(?P<pk>.*)/$', ConsultaUpdateView.as_view(), name="actualizar_consulta"),
    url(r'^consulta/eliminar/(?P<pk>.*)/$', ConsultaDeleteView.as_view(), name="eliminar_consulta"),

    #Historia
    url(r'^historia/listar/$', HistoriaListView.as_view(), name="listar_historia"),
    url(r'^historia/crear/$', HistoriaCreateView.as_view(), name="crear_historia"),
    url(r'^historia/actualizar/(?P<pk>.*)/$', HistoriaUpdateView.as_view(), name="actualizar_historia"),
    url(r'^historia/eliminar/(?P<pk>.*)/$', HistoriaDeleteView.as_view(), name="eliminar_historia"),
    url(r'^historia/detail/(?P<pk>.*)/$', HistoriaMascotaDetailView.as_view(), name='historia_detail'),

    # Mascota
    url(r'^mascota/listar/$', MascotaListView.as_view(), name="listar_mascotas"),
    url(r'^mascota/crear/$', MascotaCreateView.as_view(), name="crear_mascota"),
    url(r'^mascota/actualizar/(?P<pk>.*)/$', MascotaUpdateView.as_view(), name="actualizar_mascota"),
    url(r'^mascota/eliminar/(?P<pk>.*)/$', MascotaDeleteView.as_view(), name="eliminar_mascota"),
    url(r'^mascota/state/(?P<state>[\w\d\-]+)/(?P<pk>.*)/$',
        MascotaUpdateActiveView.as_view(), name='mascota-state'),

    #NOTAS
    url(r'^notas/listar/$', NotasListView.as_view(), name="listar_notas"),
    url(r'^notas/crear/$', NotasCreateView.as_view(), name="crear_notas"),
    url(r'^notas/actualizar/(?P<pk>.*)/$', NotasUpdateView.as_view(), name="actualizar_notas"),
    url(r'^notas/eliminar/(?P<pk>.*)/$', NotasDeleteView.as_view(), name="eliminar_notas"),

    #Vacunacion
    url(r'^vacunacion/listar/$', VacunacionListView.as_view(), name="listar_vacunacion"),
    url(r'^vacunacion/crear/$', VacunacionCreateView.as_view(), name="crear_vacunacion"),
    url(r'^vacunacion/actualizar/(?P<pk>.*)/$', VacunacionUpdateView.as_view(), name="actualizar_vacunacion"),
    url(r'^vacunacion/eliminar/(?P<pk>.*)/$', VacunacionDeleteView.as_view(), name="eliminar_vacunacion"),
]
