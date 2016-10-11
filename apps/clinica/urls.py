
from .views.mascotaviews import (MascotaListView, MascotaCreateView, MascotaUpdateView, MascotaDeleteView)

from .views.tipomascotaviews import (EspecieListView, EspecieCreateView, EspecieUpdateView)
from django.conf.urls import url
from .views.historialclinico import historialviews
urlpatterns = [
    #TIpo Mascota
    url(r'^especie/listar/$', EspecieListView.as_view(), name="listar_especie"),
    url(r'^especie/crear/$', EspecieCreateView.as_view(), name="crear_especie"),
    url(r'^especie/actualizar/(?P<pk>.*)/$', EspecieUpdateView.as_view(), name="actualizar_especie"),

    # Mascota
    url(r'^mascota/listar/$', MascotaListView.as_view(), name="listar_mascotas"),
    url(r'^mascota/crear/$', MascotaCreateView.as_view(), name="crear_mascota"),
    url(r'^mascota/actualizar/(?P<pk>.*)/$', MascotaUpdateView.as_view(), name="actualizar_mascota"),
    url(r'^mascota/eliminar/(?P<pk>.*)/$', MascotaDeleteView.as_view(), name="eliminar_mascota"),

    #historial clinico
    url(r'^atencion/historial/$', historialviews, name='historia_clinica'),
]
