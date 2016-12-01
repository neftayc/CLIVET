# coding: utf-8 _*_
from django.test import TestCase
from apps.clinica.models.mascota import Mascota
from apps.clivet.models.cliente import Cliente
from apps.params.models import Person

# Create your tests here.

class MascotaTestCase(TestCase):
    def setUp(self):
        a1 = Person.objects.create(first_name="J.K. Rowling")
        a2 = Cliente.objects.create(persona=a1)
        Mascota.objects.create(nombre="tarzan", color="negro", dueño=a2)
        Mascota.objects.create(nombre="golen", color="blanco", dueño=a2)

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        tarzan = Mascota.objects.get(nombre="tarzan")
        golen = Mascota.objects.get(nombre="golen")
        self.assertEqual(tarzan.color, 'negro')
        self.assertEqual(golen.color, 'blanco')
