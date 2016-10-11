from django.views.generic.base import TemplateView
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages


from django.shortcuts import get_object_or_404
from django.utils import timezone

# Create your views here.
def clivet(request):
    return render(request, 'clivet/dashboard.html')
