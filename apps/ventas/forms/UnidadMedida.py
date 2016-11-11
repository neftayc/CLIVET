from django import forms
from ..models.UnidadMedida import UnidadMedidaC


class UnidadMedidaForm(forms.ModelForm):
    u"""Tipo Documeto Form."""

    class Meta:
        """Meta."""

        model = UnidadMedidaC
        exclude = ()
        # widgets = {
