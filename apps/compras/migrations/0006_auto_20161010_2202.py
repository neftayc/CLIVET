# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-10 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0005_auto_20161010_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='tipodoc',
            field=models.CharField(choices=[('RUC', 'Registro Único de Comprobante'), ('DNI', 'Documento nacional de Identidad')], default='Registro Único de Comprobante', max_length=30, verbose_name='Tipo de Documento'),
        ),
    ]
