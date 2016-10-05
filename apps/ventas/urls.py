from django.conf.urls import url
from django.views.generic.base import TemplateView
from apps.ventas.views.main import ventas

urlpatterns = [
    # Examples
    url(r'ventas', ventas, name='ventas'),
]
