
from .views.mascotaviews import (MascotaListView, MascotaCreateView, MascotaUpdateView, MascotaDeleteView)

from .views.colamedicaviews import (ColaMedicaListView, ColaMedicaCreateView, ColaMedicaUpdateView, ColaMedicaDeleteView)
from django.conf.urls import url
from .views.historialclinico import historialviews

urlpatterns = [
    #Cola Medica
    url(r'^colamedica/listar/$', ColaMedicaListView.as_view(), name="listar_medica"),
    url(r'^colamedica/crear/$', ColaMedicaCreateView.as_view(), name="crear_medica"),
    url(r'^colamedica/actualizar/(?P<pk>.*)/$', ColaMedicaUpdateView.as_view(), name="actualizar_medica"),
    url(r'^colamedica/eliminar/(?P<pk>.*)/$', ColaMedicaDeleteView.as_view(), name="eliminar_medica"),

    # Mascota
    url(r'^mascota/listar/$', MascotaListView.as_view(), name="listar_mascotas"),
    url(r'^mascota/crear/$', MascotaCreateView.as_view(), name="crear_mascota"),
    url(r'^mascota/actualizar/(?P<pk>.*)/$', MascotaUpdateView.as_view(), name="actualizar_mascota"),
    url(r'^mascota/eliminar/(?P<pk>.*)/$', MascotaDeleteView.as_view(), name="eliminar_mascota"),

    #historial clinico
    url(r'^atencion/historial/$', historialviews, name='historia_clinica'),
]
