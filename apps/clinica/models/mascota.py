# _*_ coding: utf-8 _*_
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst
from django.dispatch import receiver
from django.db.models import signals
from unicodedata import normalize
from django.core.exceptions import ValidationError
from django.forms import ModelForm

CONDICION =(
    ('buena' , "Buena"),
    ('regular' , "Regular"),
    ('dema' , "Demacrada")
)

class Mascota(models.Model):

    num_historia = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    dueño = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    genero = models.BooleanField(capfirst(_('active')), default=True)
    especie = models.ForeignKey('Especie', default='1')
    raza = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    cond_corporal = models.CharField(max_length=10, choices=CONDICION, default='Buena')
    esterelizado = models.BooleanField(capfirst(_('active')), default=True)
    estado = models.BooleanField(capfirst(_('active')), default=True)
    descripcion = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Tipo Documenento Identidad"
        verbose_name_plural = "Tipos Documentos Identidad"

    def __str__(self):
                return self.nombre
