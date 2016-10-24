# coding: utf-8 _*_
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst
from django.dispatch import receiver
from django.db.models import signals
from unicodedata import normalize
from django.core.exceptions import ValidationError

from apps.clivet.models.trabajador import Trabajador
from apps.clinica.models.mascota import Mascota

# Create your models here.

class Historial(models.Model):
    num_historia = models.CharField(max_length=40)
    veterinario = models.ForeignKey(Trabajador, blank=True, null=False)
    mascota = models.OneToOneField(Mascota, verbose_name=_('Mascota'), null=True, blank=True,)
    created_ath = models.DateTimeField(_('Fecha Creada'), auto_now_add=True)

    class Meta:
        verbose_name = "Historia"
        verbose_name_plural = "Historias"

    def __str__(self):
        return "%s" % (self.num_historia)
