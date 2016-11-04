# coding: utf-8 _*_
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst
from django.dispatch import receiver
from django.db.models import signals
from unicodedata import normalize
from django.core.exceptions import ValidationError


from ..models.historia import Historial
from apps.sad.models import User

# Create your models here.

class ColaMedica(models.Model):
    historia = models.ForeignKey(Historial)
    veterinario = models.ForeignKey(User)
    fecha = models.DateField(_('Fecha Creada'), auto_now_add=True, )
    descripcion = models.CharField(max_length=100)
    estado = models.BooleanField(_('Estado de Atencion'), max_length=100, default=False)

    class Meta:
        verbose_name = "Cola Medica"
        verbose_name_plural = "Colas Medicas"

    def __str__(self):
        return "%s" % (self.historia)
