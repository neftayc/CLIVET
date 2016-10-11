#encoding: utf-8
from django import forms
from ..models.mascota import Mascota
from ..models.especie import Especie

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
         'dueño': forms.TextInput(attrs={
             'class': 'form-control', 'required': 'true',
             'placeholder': 'Ingrese al Dueño del Paciente'
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

    class Media:
        js = ('/media/js/calendar.js',
              '/media/js/DateTimeShortcuts.js',)
