from django.views.generic.base import TemplateView
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from apps.utils.decorators import permission_resource_required

# Create your views here.
def clivet(request):
    """
    """
    c = {
        'cmi' : 'clivet:index',
        'opts': _('Home'),
        'title': _('Backend Home Page.'),
    }
    return render(request, 'clivet/clivet.html', c)
