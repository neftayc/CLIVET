u"""Módulo Cita."""

from django.db import models


class Cita(models.Model):
    u"""Modelo Cita."""

    motivo = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta."""
        verbose_name = "Cita"
        verbose_name_plural = "Citas"

    def __str__(self):
        """Str."""
        return "%s" % self.motivo
