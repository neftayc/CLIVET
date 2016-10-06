from django.conf.urls import url
from .views import EspecieListView

urlpatterns = [
    # Examples
    url(r'^especie/listar/$', EspecieListView.as_view(),
        name="EspecieListView"),
    #url(r'^gg', mascotaView, name='mascotaView'),
]
