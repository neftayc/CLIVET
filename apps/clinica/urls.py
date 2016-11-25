from django.conf.urls import url



from .views.atencionviews import (AtencionListView, AtencionCreateView)
from .views.colamedicaviews import (ColaMedicaListView, ColaMedicaCreateView, ColaMedicaUpdateView, ColaMedicaDeleteView, ColasMedicasListView)
from .views.vacunacionviews import  BusquedaClientAjaxView
from .views.historiaviews import (HistoriaListView,  HistoriaMascotaDetailView, HistoriaMascotaCreateView)
from .views.mascotaviews import (MascotaListView, MascotaCreateView, MascotaUpdateView, MascotaUpdateActiveView)

urlpatterns = [
    url(r'^cliente/busqueda_ajax/$', BusquedaClientAjaxView.as_view()),
    #Atencion
    url(r'^atencion/listar/(?P<pk>\d+)/$', AtencionListView.as_view(), name="listar_atencion"),

    url(r'^atencion/crear/(?P<pk>.*)/$', AtencionCreateView.as_view(), name="crear_atencion"),

    #Cola Medica
    url(r'^colamedica/listar/$', ColaMedicaListView.as_view(), name="listar_medica"),
    url(r'^colamedica/lista/$', ColasMedicasListView.as_view(), name="lista_medica"),
    url(r'^colamedica/crear/$', ColaMedicaCreateView.as_view(), name="crear_medica"),
    url(r'^colamedica/actualizar/(?P<pk>.*)/$', ColaMedicaUpdateView.as_view(), name="actualizar_medica"),
    url(r'^colamedica/eliminar/(?P<pk>.*)/$', ColaMedicaDeleteView.as_view(), name="eliminar_medica"),

    #url(r'^colamedica/detail/(?P<pk>.*)/$', AtencionMedicaView.as_view(), name='colamedica_detail'),


    #Historia
    url(r'^historia/listar/$', HistoriaListView.as_view(), name="listar_historia"),
    url(r'^historia/mascota_add/(?P<pk>.*)/$', HistoriaMascotaCreateView.as_view(), name='crear_historiamascota'),

    url(r'^historia/detail/(?P<pk>.*)/$', HistoriaMascotaDetailView.as_view(), name='historia_detail'),

    # Mascota
    url(r'^mascota/listar/$', MascotaListView.as_view(), name="listar_mascotas"),
    url(r'^mascota/crear/$', MascotaCreateView.as_view(), name="crear_mascota"),
    url(r'^mascota/actualizar/(?P<pk>.*)/$', MascotaUpdateView.as_view(), name="actualizar_mascota"),
    url(r'^mascota/state/(?P<state>[\w\d\-]+)/(?P<pk>.*)/$',
        MascotaUpdateActiveView.as_view(), name='mascota-state'),


]
