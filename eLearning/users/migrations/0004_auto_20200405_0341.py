# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2020-04-05 03:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200405_0334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='es_mentor',
            new_name='is_professor',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='es_admin',
            new_name='is_site_admin',
        ),
    ]
