u"""Módulo Tipo Documento Form."""

from django import forms
from ..models.TipoDocumentoIdentidad import TipoDocumentoIdentidad


class TipoDocumentoIdentidadForm(forms.ModelForm):
    u"""Tipo Documeto Form."""

    class Meta:
        """Meta."""

        model = TipoDocumentoIdentidad
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
