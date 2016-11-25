# coding: utf-8 _*_
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst
from django.dispatch import receiver
from django.db.models import signals
from unicodedata import normalize
from django.core.exceptions import ValidationError
#Impors  Models
from ..models.colamedica import ColaMedica
from apps.ventas.models.Producto import Producto
from ..models.mascota import Mascota
from ..models.consulta import Diagnostico, Tratamiento, Pruebas, HallasgosClinicos

# Create your models here.
class Atencion(models.Model):
    colamedica = models.OneToOneField(ColaMedica, blank=True, unique=True  )
#Consulta

    motivo_atencion = models.CharField(max_length=300)
    temperatura = models.CharField(max_length=50)
    fc = models.CharField(max_length=50)
    fr = models.CharField(max_length=50)
    kg = models.CharField(max_length=50)
    porcentaje = models.CharField(max_length=50)
    tlc = models.CharField(max_length=50)
    anamnesis = models.CharField(max_length=200)
    hallasgos_clinicos = models.ManyToManyField(HallasgosClinicos, max_length=300)
    diagnostico = models.ManyToManyField(Diagnostico, max_length=300)
    dx = models.CharField(max_length=300)
    pronostico = models.CharField(max_length=300)
    pruebas_auxiliares = models.ManyToManyField(Pruebas, max_length=300)
    tratamiento = models.ManyToManyField(Tratamiento, max_length=300)
    observacion = models.CharField(max_length=300)

#vacunacion
    fecha_programada = models.DateTimeField(null=True, blank=True)
    vobservacion = models.CharField(max_length=100,null=True, blank=True)
    vacuna = models.ManyToManyField(Producto, max_length=100, null=True, blank=True)

#notas
    ndescripcion = models.CharField(max_length=200, default='Mascota en buen estado',null=True, blank=True)

    created_ath = models.DateTimeField(_('Fecha Creada'), auto_now_add=True)

    class Meta:
        verbose_name = "Atencion"
        verbose_name_plural = "Atenciones"

    def __str__(self):
        return "%s" % (self.colamedica)
