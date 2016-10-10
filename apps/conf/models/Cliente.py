u"""Módulo Cliente."""

from django.db import models

from apps.params.models import Person
from apps.sad.models import User


class Cliente(models.Model):
    u"""Modelo Cliente."""

    persona = models.OneToOneField(Person)
    codigo = models.CharField(max_length=9)
    parent = models.ForeignKey("self", blank=True, null=True,
                               related_name="parent")
    usuario = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta."""
        verbose_name = "Cliente"
        verbose_name_plural = "Cientes"

    def __str__(self):
        """Str."""
        return "%s %s" % (self.persona.first_name, self.persona.last_name)
