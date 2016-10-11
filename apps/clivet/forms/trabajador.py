u"""Módulo Trabajador Form."""

from django import forms
from ..models.trabajador import Trabajador


class TrabajadorForm(forms.ModelForm):
    u"""Trabajador Form."""

    class Meta:
        """Meta."""

        model = Trabajador
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
