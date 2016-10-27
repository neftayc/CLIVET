from django import forms
from ..models.Departamento import Departamento


class DepartamentoForm(forms.ModelForm):
    u"""Tipo Documeto Form."""

    class Meta:
        """Meta."""

        model = Departamento
        exclude = ()
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'col-md-8'}),
        }
