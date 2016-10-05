#encoding: utf-8
from django import forms
from .models import Especie

DUENOS_CHOICES = (
    ('rusbel', 'Rusbel Ccana Yucra'),
    ('german', 'German Castro Vilchez'),
    ('miriam', 'Mirian Calcina'),
    ('yusel', 'Yuselenin Anquise'),
)
ESPECIE_CHOICES = (
    ('rusbel', 'Rusbel Ccana Yucra'),
    ('german', 'German Castro Vilchez'),
)
RAZA_CHOICES = (
    ('pastor', 'Pastor Aleman'),
    ('peque', 'Pequeñin'),
)
COLOR_CHOICES = (
    ('rojo', 'Rojo'),
    ('azul', 'Azul'),
    ('amarillo', 'Amarillo'),
)

GENERO_CHOICES = (
    ('m', 'Macho'),
    ('h', 'Hembra'),
)

class EspecieForm(forms.Form):

    especie = forms.CharField(label='Especie', max_length=100)
    raza = forms.CharField(label='Raza', max_length=100)
    color = forms.CharField(label='Color', max_length=100)


class MascotaForm(forms.Form):

    nombre = forms.CharField(label='Nombre', max_length=100)
    num_historia = forms.CharField(label='N° Historia', max_length=100)
    dueno = forms.ChoiceField(label='Dueño', choices=DUENOS_CHOICES)
    especie = forms.ChoiceField(label='Especie', choices=ESPECIE_CHOICES)
    raza = forms.ChoiceField(label='Raza', choices=RAZA_CHOICES)
    color = forms.ChoiceField(label='Color', choices=COLOR_CHOICES)
    #f_nacimiento = forms.DateField(label='F. Nacimiento', Date)
    genero = forms.ChoiceField(label='Genero', choices=GENERO_CHOICES, widget=forms.RadioSelect())
    condicion = forms.ChoiceField(label='C.C.', choices=COLOR_CHOICES)
    esterelizado = forms.ChoiceField(label='Esterelizado', choices=COLOR_CHOICES)
    estado = forms.ChoiceField(label='Estado', choices=COLOR_CHOICES)
    descripcion = forms.CharField(label='Descripción', max_length=200, widget=forms.Textarea())
