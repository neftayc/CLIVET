from django import forms
from ..models.Producto import Producto


class ProductoForm(forms.ModelForm):
    u"""Tipo Documeto Form."""

    class Meta:
        """Meta."""

        model = Producto
        exclude = ()
        # widgets = {
