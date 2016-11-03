from django import forms
from apps.compras.models.compra import Compra


class CompraForm(forms.ModelForm):

    class Meta:
        """Meta."""

        model = Compra
        exclude = ()