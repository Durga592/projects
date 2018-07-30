# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-28 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice', '0006_auto_20180728_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='created',
        ),
        migrations.RemoveField(
            model_name='studyhall',
            name='doc',
        ),
        migrations.AddField(
            model_name='studyhall',
            name='doc_name',
            field=models.FileField(default=1, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
