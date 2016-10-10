from django import forms
from apps.compras.models.Proveedor import Proveedor


class ProveedorForm(forms.ModelForm):

    class Meta:
        """Meta."""

        model = Proveedor
        exclude = ()