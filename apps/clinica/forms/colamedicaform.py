#encoding: utf-8
from django import forms
from ..models.colamedica import ColaMedica

class ColaMedicaForm(forms.ModelForm):
    """Tipo Documeto Form."""
    class Meta:
        """Meta."""
        model = ColaMedica
        exclude = ()
        widgets = {
         'dueño': forms.Select(attrs={
         'class':"form-control", 'required': 'true'
         }),
         'mascota': forms.TextInput(attrs={
             'class': 'form-control', 'required': 'true',
             'placeholder': 'Nombre del Paciente'
         }),
         'fecha': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control', 'required': 'False',
         'placeholder': 'formato: dd/mm/yy'
         }),
        'estado':forms.Select(attrs={
        'class':"form-control", 'required': 'true'
        }),
        'descripcion':forms.Textarea(attrs={
        'class':"form-control", 'required': 'false'
        })
        }
