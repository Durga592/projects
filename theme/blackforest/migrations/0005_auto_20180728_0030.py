# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-27 19:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blackforest', '0004_auto_20180728_0019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ehall',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='ehall',
            name='created_date',
        ),
        migrations.AddField(
            model_name='ehall',
            name='created',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='ehall',
            name='createdby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='createdblackforest_ehall_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ehall',
            name='updated',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='ehall',
            name='updatedby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updatedblackforest_ehall_related', to=settings.AUTH_USER_MODEL),
        ),
    ]
