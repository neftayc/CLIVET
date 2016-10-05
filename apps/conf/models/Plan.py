u"""Módulo Plan."""

from django.db import models


class Plan(models.Model):
    u"""Modelo Plan."""

    nombre = models.CharField(max_length=90)
    estado = models.BooleanField(default=True)
    porc_primer_nivel = models.FloatField(
        blank=True, null=True, verbose_name="Porcentaje Primer Nivel")
    porc_sig_nivel = models.FloatField(
        blank=True, null=True, verbose_name="Porcentaje Siguiente Nivel")
    porc_comision = models.FloatField(
        blank=True, null=True, verbose_name="Porcentaje Comisión")
    porc_comision_nivel = models.FloatField(
        blank=True, null=True, verbose_name="Porcentaje Comísion Nivel")
    aplica_nivel = models.PositiveIntegerField()

    class Meta:
        u"""Meta."""
        verbose_name = "Plan"
        verbose_name_plural = "Planes"

    def __str__(self):
        return "%s" % (self.nombre)