# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-06-15 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_libro_doc'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='vendido',
            field=models.BooleanField(default=False),
        ),
    ]