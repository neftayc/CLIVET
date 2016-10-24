#encoding: utf-8
from django import forms
from ..models.notas import Notas

class NotasForm(forms.ModelForm):
    """Tipo Documeto Form."""
    class Meta:
        """Meta."""
        model = Notas
        exclude = ()
