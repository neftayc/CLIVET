from django.conf.urls import include, url
from .views import index

urlpatterns = [
    # Examples
    url(r'^$', index, name='base'),
]
