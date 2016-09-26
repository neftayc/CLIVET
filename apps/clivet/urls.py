from django.conf.urls import include, url
from apps.clivet.views import index

urlpatterns = [
    # Examples
    url(r'^$', index, name='base'),

]
