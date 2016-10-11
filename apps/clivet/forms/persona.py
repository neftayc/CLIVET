u"""Módulo Persona Form."""

from django import forms
from apps.params.models import Person


class PersonaForm(forms.ModelForm):
    u"""Persona Form."""

    class Meta:
        """Meta."""

        model = Person
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
