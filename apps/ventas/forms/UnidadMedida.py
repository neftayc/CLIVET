from django import forms
from ..models.UnidadMedida import UnidadMedida


class UnidadMedidaForm(forms.ModelForm):
    u"""Tipo Documeto Form."""

    class Meta:
        """Meta."""

        model = UnidadMedida
        exclude = ()
        # widgets = {
