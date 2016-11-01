from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst, get_text_list
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Field, Div, Row, HTML
from crispy_forms.bootstrap import FormActions, TabHolder, Tab

from unicodedata import normalize
from apps.utils.security import UserToken
from django.db.models import Q
from django.core.exceptions import NON_FIELD_ERRORS
from ..models.Venta import Venta


class VentaForm(forms.ModelForm):
    u"""Tipo Documeto Form."""

    class Meta:

        model = Venta
        fields = ('codigo', 'total', 'cliente', 'trabajador',)
        exclude = ()
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'trabajador': forms.Select(attrs={'class': 'form-control'}),
            'total': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Ingrese codigo De venta"
            }),
        }
