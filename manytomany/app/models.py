# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
class model1(models.Model):
	name 	=	models.CharField(max_length=255)
	def save(self, *args, **kwargs):
		for db in settings.DATABASES:
			kwargs.update({"using":db})
			if db == 'default':
				db 	=	super(model, self).save(*args, **kqargs)
			else:
				super(model, self).save(*args, **kwargs)
		return db
class model2(models.Model):
	name 	=	models.CharField(max_length=255)
	def save(self, *args, **kwargs):
		for db in settings.DATABASES:
			kwargs.update({"using":db})
			if db == 'new':
				db 	=	super(model, self).save(*args, **kqargs)
			else:
				super(model, self).save(*args, **kwargs)
		return db
class Customer(models.Model):
	name	=	models.CharField(max_length=255)

class Product(models.Model):
	name	=	models.CharField(max_length=255)

class Order(models.Model):
	product 	=	models.ManyToManyField(Product)
	customer 	=	models.ForeignKey(Customer)
	name		=	models.CharField(max_length=255)

class Trackerlogs(models.Model):
	path 		=	models.CharField(max_length=255)
	ip  		=	models.CharField(max_length=255)
	date  		=	models.DateTimeField(auto_now_add=True)