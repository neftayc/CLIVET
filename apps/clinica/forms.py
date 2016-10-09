#encoding: utf-8
from django import forms
from .models.mascota import Mascota

class MascotaForm(forms.Form):
    """Tipo Documeto Form."""

    class Meta:
        """Meta."""
        model = Mascota
        exclude = ()
        widgets = {
         'num_historia': forms.TextInput(attrs={
             'class': 'form-control', 'required': 'true',
             'placeholder': 'Ingrese Numero'
         }),
         'nombre': forms.TextInput(attrs={
             'class': 'form-control', 'required': 'true',
             'placeholder': 'Ingrese Descripcion'
         }),
         'dueño': forms.TextInput(attrs={
             'class': 'form-control', 'required': 'true',
             'placeholder': 'Ingrese Descripcion'
         })
         }
""",
'fecha_nacimiento': forms.TextInput(attrs={
    'class': 'form-control', 'required': 'true',
    'placeholder': 'Ingrese Descripcion'
}),
'genero': forms.TextInput(attrs={
    'class': 'form-control', 'required': 'true',
    'placeholder': 'Ingrese Descripcion'
}),
'especie': forms.TextInput(attrs={
    'class': 'form-control', 'required': 'true',
    'placeholder': 'Ingrese Descripcion'
}),
'raza': forms.TextInput(attrs={
    'class': 'form-control', 'required': 'true',
    'placeholder': 'Ingrese Descripcion'
}),
'color': forms.TextInput(attrs={
    'class': 'form-control', 'required': 'true',
    'placeholder': 'Ingrese Descripcion'
}),
'cond_corporal': forms.TextInput(attrs={
    'class': 'form-control', 'required': 'true',
    'placeholder': 'Ingrese Descripcion'
}),
'esterelizado': forms.TextInput(attrs={
    'class': 'form-control', 'required': 'true',
    'placeholder': 'Ingrese Descripcion'
}),
'estado': forms.TextInput(attrs={
    'class': 'form-control', 'required': 'true',
    'placeholder': 'Ingrese Descripcion'
}),
'description': forms.TextInput(attrs={
    'class': 'form-control', 'required': 'true',
    'placeholder': 'Ingrese Descripcion'
})
}"""
