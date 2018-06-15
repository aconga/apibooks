# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-06-14 05:27
from __future__ import unicode_literals

import apibooks.books.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_index=True, max_length=180, verbose_name='Nombre')),
                ('slug', models.SlugField(blank=True, max_length=96, verbose_name='slug')),
                ('editorial', models.CharField(blank=True, max_length=120, null=True)),
                ('generos', models.CharField(blank=True, max_length=120, null=True)),
                ('portada', models.ImageField(blank=True, upload_to=apibooks.books.utils.ruta_de_portadas, verbose_name='Portada')),
                ('resumen', models.TextField(blank=True)),
                ('paginas', models.IntegerField(blank=True, null=True)),
                ('fecha_de_publicacion', models.DateField(blank=True, null=True)),
                ('edicion', models.IntegerField(blank=True, null=True)),
                ('idioma', models.CharField(blank=True, max_length=120, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
