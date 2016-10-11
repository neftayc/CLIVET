u"""Módulo Trabajador."""

from django.db import models
from apps.params.models import Person
from apps.sad.models import User


class Trabajador(models.Model):
    u"""Modelo Trabajador."""
    persona = models.OneToOneField(Person)
    usuario = models.OneToOneField(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta."""
        verbose_name = "Trabajador"
        verbose_name_plural = "Trabajadores"

    def __str__(self):
        """Str."""
        return "%s %s" % (self.persona.first_name, self.persona.last_name)
