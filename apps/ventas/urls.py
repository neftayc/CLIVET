from django.conf.urls import patterns, url
from apps.ventas.views.main import ventas

urlpatterns = [url(r'^ventas', ventas.as_view()),
               # Examples

               ]
