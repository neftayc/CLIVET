# coding: utf-8 _*_
from django.test import TestCase
from apps.ventas.models.Producto import Producto
from apps.ventas.models.Departamento import Departamento
from apps.ventas.models.Categoria import Categoria
from apps.ventas.models.UnidadMedida import UnidadMedidaC
from apps.ventas.models.UnidadMedida import UnidadMedidaV

# Create your tests here.


class MascotaTestCase(TestCase):

    def setUp(self):

        a1 = Departamento.objects.create(descripcion="departamentoprueba")
        a2 = Categoria.objects.create(
            descripcion="Categoriatest", departamento=a1)
        a3 = UnidadMedidaV.objects.create(
            nombre="kilogramosprueba", simbolo="kg")
        a4 = UnidadMedidaC.objects.create(
            nombre="arobas", simbolo="@", cant_equivalencia=12, unidad_medida_venta=a3)
        Producto.objects.create(
            nombre="productoTests00000001", codigo="0001test", categoria=a2, fechaVencimiento='2026-12-12', unidad_medida=a4, precioV=2.20, precioC=2.00, existencia=0.00, MontoReal=0.00, igv=0.00)
        Producto.objects.create(
            nombre="productoTests00000002", codigo="0002test", categoria=a2, fechaVencimiento='2016-12-12', unidad_medida=a4, precioV=2.20, precioC=2.00, existencia=0.00, MontoReal=0.00, igv=0.00)

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        productoTests00000001 = Producto.objects.get(
            nombre="productoTests00000001")
        productoTests00000002 = Producto.objects.get(
            nombre="productoTests00000002")
        self.assertEqual(productoTests00000001.codigo, '0001test')
        self.assertEqual(productoTests00000002.codigo, '0002test')
