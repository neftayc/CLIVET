#encoding: utf-8
from django import forms
from ..models.consulta import Consulta

class ConsultaForm(forms.ModelForm):
    """Tipo Documeto Form."""
    class Meta:
        """Meta."""
        model = Consulta
        exclude = ()
