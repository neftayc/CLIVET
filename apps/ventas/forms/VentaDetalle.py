from django import forms
from ..models.Venta_Detalle import Detalle_Venta


class Detalle_VentaForm(forms.ModelForm):
    u"""Tipo Documeto Form."""

    class Meta:
        """Meta."""

        model = Detalle_Venta
        fileds = ('producto', 'venta', 'cantidad', 'igv', 'importe')
        exclude = ()
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'venta': forms.Select(attrs={'class': 'form-control'}),
            'importe': forms.Select(attrs={'class': 'form-control'}),
            'igv': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.Select(attrs={'class': 'form-control'}),
        }
