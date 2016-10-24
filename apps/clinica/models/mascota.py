# coding: utf-8 _*_
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst
from django.dispatch import receiver
from django.db.models import signals
from unicodedata import normalize
from django.core.exceptions import ValidationError


from apps.clivet.models.cliente import Cliente

CONDICION =(
    ('Buena' , "Buena"),
    ('Regular' , "Regular"),
    ('Demacrada' , "Demacrada")
)
TIPO_MASCOTA =(
    ('Perro' , "Perro"),
    ('Gato' , "Gato"),
    ('Roedor' , "Roedor")
)

BOOL_GENERO= (
    ('Macho', "Macho"),
    ('Hembra', "Hembra")
)
BOOL= (
    ('Si', "Sí"),
    ('No', "No")
)
BOOL_ESTADO= (
    ('Vivo', "Vivo"),
    ('Fallecio', "Fallecio")
)
class Mascota(models.Model):

    nombre = models.CharField(max_length=100)
    dueño = models.ForeignKey(Cliente, default='1')
    fecha_nacimiento = models.DateTimeField(capfirst(_('Fecha Nacimiento')), null=True, blank=True)
    genero = models.CharField(max_length=10, choices=BOOL_GENERO, default='Macho')
    especie = models.CharField(max_length=10, choices=TIPO_MASCOTA, default='Perro')
    raza = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    cond_corporal = models.CharField(max_length=10, choices=CONDICION, default='Buena')
    esterelizado = models.BooleanField(capfirst(_('Esterelizado...?')), default=True)
    is_active = models.BooleanField(capfirst(_('active')), default=True)
    is_actived = models.BooleanField(_('Actived'), default=False)
    descripcion = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"

    def __str__(self):
        return "%s" % (self.nombre)
