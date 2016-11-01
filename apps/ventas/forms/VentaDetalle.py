from django import forms
from ..models.Venta_Detalle import Detalle_Venta


class Detalle_VentaForm(forms.ModelForm):
    u"""Tipo Documeto Form."""

    class Meta:
        """Meta."""

        model = Detalle_Venta
        fileds = ('producto', 'venta',
                  'cantidad', 'igv', 'importe')
        exclude = ()
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'venta': forms.Select(attrs={'class': 'form-control'}),
            'importe': forms.TextInput(attrs={'class': 'form-control'}),
            'igv': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
        }
