from django import forms
from ..models.Venta_Detalle import  Detalle_Venta


class Detalle_VentaForm(forms.ModelForm):
    u"""Tipo Documeto Form."""

    class Meta:
        """Meta."""

        model = Detalle_Venta
        exclude = ()
        # widgets = {
