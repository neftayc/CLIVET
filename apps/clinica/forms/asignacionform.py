#encoding: utf-8
from django import forms
from ..models.vacunacion import Vacunacion

class AsignacionForm(forms.ModelForm):
    """Tipo Documeto Form."""
    class Meta:
        """Meta."""
        model = Vacunacion
        exclude = ()