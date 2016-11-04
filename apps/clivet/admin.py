from django.contrib import admin

# Register your models here.
from .models.cliente import Cliente

admin.site.register(Cliente)
