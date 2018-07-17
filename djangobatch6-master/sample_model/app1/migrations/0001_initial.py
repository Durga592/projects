# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-12 03:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.TextField()),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('cost', models.IntegerField()),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('sal_type', models.CharField(choices=[('online', 'Online payment'), ('cod', 'CASH ON DELIVERY')], max_length=6)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Customer')),
                ('product', models.ManyToManyField(to='app1.Product')),
            ],
            options={
                'db_table': 'salesorders',
            },
        ),
    ]
