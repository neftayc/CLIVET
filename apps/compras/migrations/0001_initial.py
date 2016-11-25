# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-25 15:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fe_compra', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de compra')),
                ('comprobante', models.ImageField(blank=True, null=True, upload_to='persons')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Total')),
            ],
            options={
                'verbose_name_plural': 'Compras',
                'verbose_name': 'Compra',
            },
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('precio_total', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Precio Total')),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.Compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.Producto')),
            ],
            options={
                'verbose_name_plural': 'Detalles Compra',
                'verbose_name': 'Detalle Compra',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipodoc', models.CharField(choices=[('RUC', 'Registro Único de Comprobante'), ('DNI', 'Documento nacional de Identidad')], default='Registro Único de Comprobante', max_length=30, verbose_name='Tipo de Documento')),
                ('numdoc', models.IntegerField(max_length=30, verbose_name='Número de documento')),
                ('razon_social', models.CharField(max_length=50, verbose_name='Razon social')),
                ('representante_legal', models.CharField(max_length=50, verbose_name='Representante legal')),
                ('direccion', models.CharField(max_length=30, verbose_name='Direccion')),
                ('telefono', models.IntegerField(blank=True, max_length=9, null=True, verbose_name='Telefono')),
                ('email', models.EmailField(blank=True, max_length=30, null=True, verbose_name='Email')),
                ('enti_bancaria', models.CharField(blank=True, max_length=30, null=True, verbose_name='Entidad bancaria')),
                ('num_cuenta', models.IntegerField(blank=True, max_length=30, null=True, verbose_name='Número de cuenta')),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Proveedores',
                'verbose_name': 'Proveedor',
            },
        ),
        migrations.AddField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.Proveedor'),
        ),
        migrations.AddField(
            model_name='compra',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
