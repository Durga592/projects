# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-31 17:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagi_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='name',
            new_name='full_name',
        ),
    ]
