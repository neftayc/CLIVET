from django import forms
from ..models.Venta import  Venta


class VentaForm(forms.ModelForm):
    u"""Tipo Documeto Form."""

    class Meta:
        """Meta."""

        model = Venta
        exclude = ()
        # widgets = {
