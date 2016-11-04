# coding: utf-8 _*_
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst
from django.dispatch import receiver
from django.db.models import signals
from unicodedata import normalize
from django.core.exceptions import ValidationError
from ..models.colamedica import ColaMedica
from ..models.consulta import Consulta
from ..models.notas import Notas
from ..models.vacunacion import Vacunacion
from ..models.mascota import Mascota


VACUNA = (
    ('VACUNA1', "Vacuna1"),
    ('VACUNA2', "Vacuna2"),
    ('VACUNA3', "Vacuna3"),
    ('VACUNA4', "Vacuna4")
)

# Create your models here.
class Atencion(models.Model):
    colamedica = models.ForeignKey(ColaMedica, blank=True, unique=True  )
#Consulta
    anamnesis = models.CharField(max_length=200)
    diagnostico = models.CharField(max_length=300)
    dx = models.CharField(max_length=300)
    hallasgos_clinicos = models.CharField(max_length=100)
    motivo_atencion = models.CharField(max_length=300)
    observacion = models.CharField(max_length=300)
    pronostico = models.CharField(max_length=300)
    pruebas_auxiliares = models.CharField(max_length=300)
    tratamiento = models.CharField(max_length=300)

#vacunacion
    fecha_programada = models.DateTimeField(null=True, blank=True)
    vobservacion = models.CharField(max_length=100,null=True, blank=True)
    vacuna = models.CharField(max_length=100,choices=VACUNA, null=True, blank=True)

#notas
    ndescripcion = models.CharField(max_length=200, default='Mascota en buen estado',null=True, blank=True)

    created_ath = models.DateTimeField(_('Fecha Creada'), auto_now_add=True)

    class Meta:
        verbose_name = "Atencion"
        verbose_name_plural = "Atenciones"

    def __str__(self):
        return "%s" % (self.colamedica)