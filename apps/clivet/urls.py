from django.conf.urls import url
from apps.clivet.views.main import clivet

urlpatterns = [
    # Examples
    url(r'^clivet', clivet, name='clivet'),
]
