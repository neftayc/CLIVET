from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.


class ventas(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, "index.html")

    def post(self, request, *args, **kwargs):
        return render(request, "index.html")
