u"""Módulo Cliente."""

from django.db import models
from apps.params.models import Person


class Cliente(models.Model):
    u"""Modelo Cliente."""
    persona = models.OneToOneField(Person)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta."""
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        """Str."""
        return "%s %s" % (self.persona.first_name, self.persona.last_name)
