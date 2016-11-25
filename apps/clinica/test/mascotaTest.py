from django.test import TestCase
from ..models.mascota import Mascota

class MascotaTestCase(TestCase):
    def setUp(self):
        Mascota.objects.create(name="lion", sound="roar")
        Mascota.objects.create(name="cat", sound="meow")

    def test_mascotas_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
