u"""Módulo Cliente Form."""

from django import forms
from ..models.cliente import Cliente


class ClienteForm(forms.ModelForm):
    u"""Cliente Form."""
    nombre = forms.CharField()
    apellido = forms.CharField()

    class Meta:
        """Meta."""

        model = Cliente
        exclude = ('persona',)
        # widgets = {
        #     'numero': forms.TextInput(attrs={
        #         'class': 'form-control', 'required': 'true',
        #         'placeholder': 'Ingrese Número'
        #     }),
        #     'descripcion': forms.TextInput(attrs={
        #         'class': 'form-control', 'required': 'true',
        #         'placeholder': 'Ingrese Descripción'
        #     })
        # }
