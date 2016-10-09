from django.views.generic.base import TemplateView
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages


from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Vacuna

# Create your views here.
def clivet(request):
    vacuna = Vacuna.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'clivet/clivet.html', {'vacuna': vacuna})
