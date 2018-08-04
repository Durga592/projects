# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Customer(models.Model):
	name	=	models.CharField(max_length=255)

class Product(models.Model):
	name	=	models.CharField(max_length=255)

class Order(models.Model):
	product 	=	models.ManyToManyField(Product)
	customer 	=	models.ForeignKey(Customer)
	#name		=	models.CharField(max_length=255)
	date 		=	models.DateTimeField()