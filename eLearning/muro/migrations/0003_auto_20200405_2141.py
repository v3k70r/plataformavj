# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2020-04-05 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muro', '0002_auto_20200405_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='imagen',
            field=models.ImageField(default='imagen.png', upload_to='portadas'),
        ),
    ]
