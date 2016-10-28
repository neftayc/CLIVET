u"""Módulo Cita."""

from django import forms
from ..models.cita import Cita


class CitaForm(forms.ModelForm):
    u"""Cita."""

    class Meta:
        """Meta."""

        model = Cita
        exclude = ()
