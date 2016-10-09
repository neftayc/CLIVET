from django.conf.urls import url
from .mascotaviews import MascotaListView

urlpatterns = [
    # Examples
    url(r'^mascota/listar/$', MascotaListView.as_view(),
        name="MascotaListView"),
    #url(r'^gg', mascotaView, name='mascotaView'),
]
