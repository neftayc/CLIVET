from django.conf.urls import url
from apps.ventas.views.main import Ventas


urlpatterns = [
    # Examples
    url(r'ventas', Ventas.as_view()),
]
