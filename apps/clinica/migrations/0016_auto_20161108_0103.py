# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-08 01:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0015_auto_20161108_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colamedica',
            name='historia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.Historial'),
        ),
    ]
