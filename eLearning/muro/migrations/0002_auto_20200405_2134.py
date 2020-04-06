# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2020-04-05 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='imagen',
            field=models.ImageField(default='users/static_in_users/static_files/img/imagen.png', upload_to='portadas'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='comment_count',
            field=models.IntegerField(default=0),
        ),
    ]
