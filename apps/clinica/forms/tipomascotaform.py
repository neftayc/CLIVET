#encoding: utf-8
from django import forms
from ..models.especie import Especie

class EspecieForm(forms.ModelForm):
    """Tipo Documeto Form."""
    class Meta:
        """Meta."""
        model = Especie
        exclude = ()
        widgets = {
            'descripcion': forms.TextInput(attrs={
             'class': 'form-control', 'required': 'true',
             'placeholder': 'Ingrese el tipo de mascota'
         })
         }
