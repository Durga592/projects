# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-01 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eexpenses',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
