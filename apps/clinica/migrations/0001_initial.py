# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-05 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especie', models.CharField(max_length=100)),
                ('raza', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
            ],
        ),
    ]
