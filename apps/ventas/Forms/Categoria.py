from django import forms
from ..models.Categoria import Categoria


class CategoriaForm(forms.ModelForm):
    u"""Tipo Documeto Form."""

    class Meta:
        """Meta."""

        model = Categoria
        exclude = ()
        # widgets = {
