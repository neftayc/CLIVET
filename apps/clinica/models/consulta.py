# coding: utf-8 _*_
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst
from django.dispatch import receiver
from django.db.models import signals
from unicodedata import normalize
from django.core.exceptions import ValidationError

from apps.clinica.models.mascota import Mascota
# Create your models here.

class Consulta(models.Model):
    mascota = models.ForeignKey(Mascota, blank=True)
    anamnesis = models.CharField(max_length=200)
    diagnostico = models.CharField(max_length=300)
    dx = models.CharField(max_length=300)
    hallasgos_clinicos = models.CharField(max_length=100)
    motivo_atencion = models.CharField(max_length=300)
    observacion = models.CharField(max_length=300)
    pronostico = models.CharField(max_length=300)
    pruebas_auxiliares = models.CharField(max_length=300)
    tratamiento = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"

    def __str__(self):
        return "%s" % (self.anamnesis)
