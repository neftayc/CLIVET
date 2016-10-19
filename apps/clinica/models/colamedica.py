# coding: utf-8 _*_
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst
from django.dispatch import receiver
from django.db.models import signals
from unicodedata import normalize
from django.core.exceptions import ValidationError

from apps.clivet.models.cliente import Cliente
from ..models.mascota import Mascota

# Create your models here.

ESTADOS = (
    ('normal', "Normal"),
    ('emergencia', "Emergencia"),
    ('reservado', "Reservado")
)

class ColaMedica(models.Model):

    dueño = models.ForeignKey(Cliente)
    mascota = models.ForeignKey(Mascota)
    fecha = models.DateTimeField()
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=100,choices=ESTADOS)

    class Meta:
        verbose_name = "ColaMedica"
        verbose_name_plural = "ColasMedicas"

    def __str__(self):
        return "%s" % (self.dueño)
