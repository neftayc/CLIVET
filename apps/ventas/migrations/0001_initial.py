# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import apps.ventas.models.Categoria
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clivet', '0002_auto_20161027_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
                'verbose_name': 'Categoria',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Departamentos',
                'verbose_name': 'Departamento',
            },
        ),
        migrations.CreateModel(
            name='Detalle_Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('igv', models.DecimalField(decimal_places=2, max_digits=20)),
                ('importe', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
            options={
                'verbose_name_plural': 'Detalles Venta',
                'verbose_name': 'Detalle Venta',
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
                'verbose_name_plural': 'Productos',
                'verbose_name': 'Producto',
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
                'verbose_name_plural': 'Unidad de Medidas',
                'verbose_name': 'Unidad de Medida',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechav', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clivet.Cliente')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Ventas',
                'verbose_name': 'Venta',
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
