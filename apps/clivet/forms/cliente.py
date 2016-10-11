u"""Módulo Cliente Form."""

from django import forms
from ..models.cliente import Cliente


class ClienteForm(forms.ModelForm):
    u"""Cliente Form."""

    class Meta:
        """Meta."""

        model = Cliente
        exclude = ()
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
