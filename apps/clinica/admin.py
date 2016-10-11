#encoding: utf-8
from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _

# models
from .models.especie import Especie
from .models.mascota import Mascota


admin.site.register(Mascota)
admin.site.register(Especie)
