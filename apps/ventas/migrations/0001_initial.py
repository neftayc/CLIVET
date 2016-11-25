# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-25 03:10
from __future__ import unicode_literals

import apps.ventas.models.Categoria
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clivet', '0001_initial'),
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
            name='Detalle_Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('importe', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
            options={
                'verbose_name': 'Detalle Venta',
                'verbose_name_plural': 'Detalles Venta',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('codigo', models.CharField(blank=True, help_text='El codigo debe ser lalala', max_length=50, unique=True, verbose_name='Código')),
                ('fechaVencimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de vencimiento')),
                ('precioV', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio de venta')),
                ('precioC', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio de Compra')),
                ('existencia', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Cantidad de Productos')),
                ('MontoReal', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Monto Real')),
                ('igv', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='IGV')),
                ('categoria', models.ForeignKey(on_delete=apps.ventas.models.Categoria.Categoria, to='ventas.Categoria')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='UnidadMedidaC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('simbolo', models.CharField(max_length=10)),
                ('cant_equivalencia', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Cantidad de equivalencia')),
            ],
            options={
                'verbose_name': 'Unidad de medida Compra',
                'verbose_name_plural': 'Unidad de medidas Compras',
            },
        ),
        migrations.CreateModel(
            name='UnidadMedidaV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('simbolo', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Unidad de medida Venta',
                'verbose_name_plural': 'Unidad de medidas Ventas',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechav', models.DateField(auto_now_add=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('igv', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clivet.Cliente')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
        migrations.AddField(
            model_name='unidadmedidac',
            name='unidad_medida_venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.UnidadMedidaV', verbose_name='Unidad de medida para ventas'),
        ),
        migrations.AddField(
            model_name='producto',
            name='unidad_medida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unidad_de_medida', to='ventas.UnidadMedidaC', verbose_name='U. medida compra a ventas'),
        ),
        migrations.AddField(
            model_name='detalle_venta',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.Producto'),
        ),
        migrations.AddField(
            model_name='detalle_venta',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.Venta'),
        ),
        migrations.AddField(
            model_name='categoria',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.Departamento'),
        ),
    ]
