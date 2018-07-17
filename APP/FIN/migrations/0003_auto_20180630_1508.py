# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-30 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FIN', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userdets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='USER FULL NAME')),
                ('username', models.CharField(max_length=250, verbose_name='USER LOGIN NAME')),
                ('password', models.CharField(max_length=250, verbose_name='USER PASSWORD')),
                ('mailid', models.CharField(max_length=250, verbose_name='USER MAIL ID')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
