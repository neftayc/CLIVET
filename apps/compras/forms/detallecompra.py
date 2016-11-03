from django import forms
from apps.compras.models.detallecompra import DetalleCompra


class DetalleCompraForm(forms.ModelForm):

    class Meta:
        """Meta."""

        model = detallecompra
        exclude = ()