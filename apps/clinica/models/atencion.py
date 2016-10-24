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

# Create your models here.

class Atencion(models.Model):
    mascota = models.ForeignKey(Mascota)
    colamedica = models.OneToOneField(ColaMedica, blank=True, unique=True  )
    consulta = models.ForeignKey(Consulta, null=True, blank=True)
    notas = models.ForeignKey(Notas, null=True, blank=True)
    vacunacion = models.ForeignKey(Vacunacion, null=True, blank=True)
    created_ath = models.DateTimeField(_('Fecha Creada'), auto_now_add=True)

    class Meta:
        verbose_name = "Atencion"
        verbose_name_plural = "Atenciones"

    def __str__(self):
        return "%s" % (self.colamedica)
