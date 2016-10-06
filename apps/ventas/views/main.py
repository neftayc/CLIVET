from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.


class Ventas(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'ventas/index.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'ventas/index.html')
