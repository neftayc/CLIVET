from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render

# Create your views here.


def clivet(request):
    """
    """
    c = {
        'cmi': 'clivet:index',
        'opts': _('Home'),
        'title': _('Backend Home Page.'),
    }
    return render(request, 'main/dashboard.html', c)
