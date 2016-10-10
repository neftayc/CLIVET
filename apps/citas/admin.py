from django.contrib import admin

# Register your models here.
from .models.cliente import Cliente
from .models.eventos import Evento
from .models.cita import Cita
from .models.trabajador import Trabajador

admin.site.register(Cliente)
admin.site.register(Evento)
admin.site.register(Cita)
admin.site.register(Trabajador)
