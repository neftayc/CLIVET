from django.contrib import admin

# Register your models here.
from .models.trabajador import Trabajador
from .models.cliente import Cliente

admin.site.register(Trabajador)
admin.site.register(Cliente)
