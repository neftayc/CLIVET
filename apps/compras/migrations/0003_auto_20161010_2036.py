# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-10 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_auto_20161010_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='tipodoc',
            field=models.CharField(choices=[('RUC', 'Registro Unico de Comprobante'), ('DNI', 'Documento nacional de Identidad')], max_length=30),
        ),
    ]
