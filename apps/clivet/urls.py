from django.conf.urls import url
from django.views.generic.base import TemplateView
from .views import clivet

urlpatterns = [
    # Examples
    url(r'^clivet', clivet, name='clivet'),
]
