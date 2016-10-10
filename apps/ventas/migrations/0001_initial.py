# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-10 22:58
from __future__ import unicode_literals

import apps.ventas.models.Categoria
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('codigo', models.CharField(max_length=50, unique=True, verbose_name='Código')),
                ('fechaVencimiento', models.DateField(verbose_name='Fecha de Vencimiento')),
                ('precioV', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio de venta')),
                ('precioC', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio de Compra')),
                ('existencia', models.IntegerField(verbose_name='Cantidad de Productos')),
                ('MontoReal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Monto Real')),
                ('igv', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='IGV')),
                ('categoria', models.ForeignKey(on_delete=apps.ventas.models.Categoria.Categoria, to='ventas.Categoria')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('simbolo', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'verbose_name': 'Unidad de Medida',
                'verbose_name_plural': 'Unidad de Medidas',
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='unidadMedidaC',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compras', to='ventas.UnidadMedida', verbose_name='Unidad de medida de Compras'),
        ),
        migrations.AddField(
            model_name='producto',
            name='unidadMedidaV',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ventas', to='ventas.UnidadMedida', verbose_name='Unidad de medida de Ventas'),
        ),
        migrations.AddField(
            model_name='categoria',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.Departamento'),
        ),
    ]
