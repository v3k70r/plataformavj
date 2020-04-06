# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2020-04-05 19:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('texto', models.TextField(max_length=1000)),
                ('author', models.CharField(max_length=30)),
                ('comment_count', models.IntegerField(default=1)),
                ('stamp_created', models.DateTimeField(auto_now_add=True)),
                ('stamp_updated', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('author', models.CharField(max_length=30)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('comment_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muro.Anuncio')),
            ],
        ),
    ]
