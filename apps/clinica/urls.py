from django.conf.urls import url
from .views import especieView, mascotaView

urlpatterns = [
    # Examples
    url(r'^clinica', especieView, name='especieView'),
    url(r'^gg', mascotaView, name='mascotaView'),
]
