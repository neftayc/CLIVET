# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-25 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atencion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo_atencion', models.CharField(max_length=300)),
                ('temperatura', models.CharField(max_length=50)),
                ('fc', models.CharField(max_length=50)),
                ('fr', models.CharField(max_length=50)),
                ('kg', models.CharField(max_length=50)),
                ('porcentaje', models.CharField(max_length=50)),
                ('tlc', models.CharField(max_length=50)),
                ('anamnesis', models.CharField(max_length=200)),
                ('dx', models.CharField(max_length=300)),
                ('pronostico', models.CharField(max_length=300)),
                ('observacion', models.CharField(max_length=300)),
                ('fecha_programada', models.DateTimeField(blank=True, null=True)),
                ('vobservacion', models.CharField(blank=True, max_length=100, null=True)),
                ('ndescripcion', models.CharField(blank=True, default='Mascota en buen estado', max_length=200, null=True)),
                ('created_ath', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creada')),
            ],
            options={
                'verbose_name_plural': 'Atenciones',
                'verbose_name': 'Atencion',
            },
        ),
        migrations.CreateModel(
            name='ColaMedica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='Fecha Creada')),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.BooleanField(default=False, max_length=100, verbose_name='Estado de Atencion')),
            ],
            options={
                'verbose_name_plural': 'Colas Medicas',
                'verbose_name': 'Cola Medica',
            },
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HallasgosClinicos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_historia', models.CharField(max_length=40, unique=True)),
                ('created_ath', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creada')),
            ],
            options={
                'verbose_name_plural': 'Historias',
                'verbose_name': 'Historia',
            },
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateTimeField(blank=True, null=True, verbose_name='Fecha Nacimiento')),
                ('genero', models.CharField(choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')], default='Macho', max_length=10)),
                ('especie', models.CharField(choices=[('Perro', 'Perro'), ('Gato', 'Gato'), ('Roedor', 'Roedor')], default='Perro', max_length=10)),
                ('raza', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('cond_corporal', models.CharField(choices=[('Buena', 'Buena'), ('Regular', 'Regular'), ('Demacrada', 'Demacrada')], default='Buena', max_length=10)),
                ('esterelizado', models.BooleanField(default=True, verbose_name='Esterelizado...?')),
                ('historia', models.BooleanField(default=False, verbose_name='Historia')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_actived', models.BooleanField(default=False, verbose_name='Actived')),
                ('descripcion', models.CharField(max_length=200)),
                ('caracter', models.CharField(blank=True, choices=[('tranquilo', 'Tranquilo'), ('agresivo', 'Agresivo'), ('nervioso', 'Nervioso')], max_length=100, null=True)),
                ('actividad', models.CharField(blank=True, choices=[('alta', 'Alta'), ('normal', 'Normal'), ('baja', 'Baja')], max_length=100, null=True)),
                ('habitar', models.CharField(blank=True, choices=[('casa', 'Casa'), ('azotea', 'Azotea'), ('campo', 'Campo'), ('patio', 'Patio'), ('criadero', 'Criadero'), ('jardin', 'Jardin'), ('calle', 'Calle')], max_length=100, null=True)),
                ('alimentacion', models.CharField(blank=True, choices=[('balanceada', 'Balanceada seca'), ('lata', 'Lata'), ('casera', 'Casera'), ('huevos', 'Huevos'), ('huevos', 'Otros')], max_length=100, null=True)),
                ('aptitup', models.CharField(blank=True, choices=[('compañia', 'Compañia'), ('guardia', 'Guardia'), ('trabajo', 'Trabajo'), ('deporte', 'Deporte'), ('casa', 'Casa')], max_length=100, null=True)),
                ('convive', models.CharField(blank=True, choices=[('Si', 'Sí'), ('No', 'No')], max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Mascotas',
                'verbose_name': 'Mascota',
            },
        ),
        migrations.CreateModel(
            name='Pruebas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
    ]
