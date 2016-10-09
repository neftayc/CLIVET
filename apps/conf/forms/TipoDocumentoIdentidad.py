"""Modulo Tipo Documento Form."""

from django import forms
from ..models.TipoDocumentoIdentidad import TipoDocumentoIdentidad


class TipoDocumentoIdentidadForm(forms.ModelForm):
    """Tipo Documeto Form."""

    class Meta:
        """Meta."""

        model = TipoDocumentoIdentidad
        exclude = ()
        widgets = {
         'numero': forms.TextInput(attrs={
             'class': 'form-control', 'required': 'true',
             'placeholder': 'Ingrese Numero'
         }),
         'descripcion': forms.TextInput(attrs={
             'class': 'form-control', 'required': 'true',
             'placeholder': 'Ingrese Descripcion'
         })
        }
