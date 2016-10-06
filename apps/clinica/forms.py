#encoding: utf-8
from django import forms
from .models import Especie


class EspecieForm(forms.Form):
    """Tipo Documeto Form."""

    class Meta:
        """Meta."""

        model = Especie
        exclude = ()
        widgets = {
         'especie': forms.TextInput(attrs={
             'class': 'form-control', 'required': 'true',
             'placeholder': 'Ingrese Numero'
         }),
         'raza': forms.TextInput(attrs={
             'class': 'form-control', 'required': 'true',
             'placeholder': 'Ingrese Descripcion'
         }),
         'color': forms.TextInput(attrs={
             'class': 'form-control', 'required': 'true',
             'placeholder': 'Ingrese Descripcion'
         })
        }
