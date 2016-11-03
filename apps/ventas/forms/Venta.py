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
from apps.ventas.models.Producto import Producto


class VentaForm(forms.ModelForm):
    u"""Tipo Documeto Form."""
    producto = forms.ModelChoiceField(
        queryset=Producto.objects.all(), required=False, label="", help_text="")
    data_venta = forms.CharField(
        required=False,  widget=forms.TextInput(attrs={'type': 'hidden'}))
    producto = forms.CharField(label="",
                               widget=forms.TextInput(attrs={'class': 'typeahead'}))

    class Meta:

        model = Venta
        fields = ('total', 'cliente',)
        exclude = ()
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'total': forms.TextInput(attrs={'class': 'form-control'}),
        }
