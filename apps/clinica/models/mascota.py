# coding: utf-8 _*_
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst
from django.dispatch import receiver
from django.db.models import signals
from unicodedata import normalize
from django.core.exceptions import ValidationError


from apps.clivet.models.cliente import Cliente

CONDICION = (
    ('Buena', "Buena"),
    ('Regular', "Regular"),
    ('Demacrada', "Demacrada")
)
TIPO_MASCOTA = (
    ('Perro', "Perro"),
    ('Gato', "Gato"),
    ('Roedor', "Roedor")
)

BOOL_GENERO = (
    ('Macho', "Macho"),
    ('Hembra', "Hembra")
)

CARACTER = (
    ('tranquilo', "Tranquilo"),
    ('agresivo', "Agresivo"),
    ('nervioso', "Nervioso")
)

ACTIVIDAD = (
    ('alta', "Alta"),
    ('normal', "Normal"),
    ('baja', "Baja")
)

HABITAT = (
    ('casa', "Casa"),
    ('azotea', "Azotea"),
    ('campo', "Campo"),
    ('patio', "Patio"),
    ('criadero', "Criadero"),
    ('jardin', "Jardin"),
    ('calle', "Calle")
)

ALIMENTACION = (
    ('balanceada', "Balanceada seca"),
    ('lata', "Lata"),
    ('casera', "Casera"),
    ('huevos', "Huevos"),
    ('huevos', "Otros")
)

APTITUP = (
    ('compañia', "Compañia"),
    ('guardia', "Guardia"),
    ('trabajo', "Trabajo"),
    ('deporte', "Deporte"),
    ('casa', "Casa")
)

CONVIVE = (
    ('Si', "Sí"),
    ('No', "No")
)

class Mascota(models.Model):

    nombre = models.CharField(max_length=100)
    dueño = models.ForeignKey(Cliente)
    fecha_nacimiento = models.DateTimeField(
        capfirst(_('Fecha Nacimiento')), null=True, blank=True)
    genero = models.CharField(
        max_length=10, choices=BOOL_GENERO, default='Macho')
    especie = models.CharField(
        max_length=10, choices=TIPO_MASCOTA, default='Perro')
    raza = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    cond_corporal = models.CharField(
        max_length=10, choices=CONDICION, default='Buena')
    esterelizado = models.BooleanField(
        capfirst(_('Esterelizado...?')), default=True)
    historia = models.BooleanField(capfirst(_('Historia')), default=False)
    is_active = models.BooleanField(capfirst(_('active')), default=True)
    is_actived = models.BooleanField(_('Actived'), default=False)
    descripcion = models.CharField(max_length=200)

#reseña de la amscota
    caracter = models.CharField(max_length=100, choices=CARACTER ,null=True, blank=True)
    actividad = models.CharField(max_length=100, choices=ACTIVIDAD ,null=True, blank=True)
    habitar = models.CharField(max_length=100, choices=HABITAT ,null=True, blank=True)
    alimentacion = models.CharField(max_length=100, choices=ALIMENTACION , null=True, blank=True)
    aptitup = models.CharField(max_length=100, choices=APTITUP ,null=True, blank=True)
    convive = models.CharField(max_length=100, choices=CONVIVE ,null=True, blank=True)

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"

    def __str__(self):
        return "%s" % (self.nombre)
