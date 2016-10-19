# coding: utf-8 _*_
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst
from django.dispatch import receiver
from django.db.models import signals
from unicodedata import normalize
from django.core.exceptions import ValidationError


VACUNA = (
    ('VACUNA1', "Vacuna1"),
    ('VACUNA2', "Vacuna2"),
    ('VACUNA3', "Vacuna3"),
    ('VACUNA4', "Vacuna4")
)

class Vacunacion(models.Model):

    fecha_programada = models.DateTimeField()
    Observacion = models.CharField(max_length=100)
    vacuna = models.CharField(max_length=100,choices=VACUNA)

    class Meta:
        verbose_name = "Vacunacion"
        verbose_name_plural = "Vacunaciones"

    def __str__(self):
        return "%s" % (self.vacuna)
