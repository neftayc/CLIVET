from django.db import models
from django.utils import timezone

# Create your models here.

class Vacuna(models.Model):
    vacuna_aplicada = models.CharField(max_length=200)
    observacion = models.TextField(max_length=400)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.vacuna_aplicada
