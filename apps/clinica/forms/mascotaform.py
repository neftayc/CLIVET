#encoding: utf-8
from django import forms

from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst, get_text_list
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Field, Div, Row, HTML
from crispy_forms.bootstrap import FormActions, TabHolder, Tab

from apps.utils.forms import smtSave, btnCancel, btnReset

from ..models.mascota import Mascota

class MascotaForm(forms.ModelForm):
    """Tipo Documeto Form."""
    class Meta:
        """Meta."""
        model = Mascota
        exclude = ()
        widgets = {
            'num_historia': forms.TextInput(attrs={
             'class': 'form-control', 'required': 'true',
             'placeholder': 'Ingrese Numero de Historia clinica'
         }),
         'nombre': forms.TextInput(attrs={
             'class': 'form-control', 'required': 'true',
             'placeholder': 'Nombre del Paciente'
         }),
         'dueño': forms.Select(attrs={
         'class':"form-control", 'required': 'true'
         }),
         'fecha_nacimiento': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control', 'required': 'False',
         'placeholder': 'formato: dd/mm/yy'
         }),
         'genero':forms.RadioSelect(attrs={
         'class':"radio-inline", 'required': 'true'
         }),
        'especie' : forms.Select(attrs={
        'class':"form-control", 'required': 'true'
        }),
        'raza':forms.TextInput(attrs={
        'class':"form-control", 'required': 'true'
        }),
        'color':forms.TextInput(attrs={
        'class':"form-control", 'required': 'true'
        }),
        'cond_corporal':forms.Select(attrs={
        'class':"form-control", 'required': 'true'
        }),
        'esterelizado':forms.Select(attrs={
        'class':"form-control", 'required': 'true'
        }),
        'estado':forms.Select(attrs={
        'class':"form-control", 'required': 'true'
        }),
        'descripcion':forms.Textarea(attrs={
        'class':"form-control", 'required': 'false'
        })
        }
