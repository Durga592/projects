# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Ehall(models.Model):
	name	=	models.CharField(max_length=250)
	area	=	models.TextField()
	class Meta:
		db_table	=	'e_hall'
	def __str__(self):
		return "%s | %s"%(self.name, self.area)

class Eexpenses(models.Model):
	ehall 	=	models.ForeignKey(Ehall)
	date 	=	models.DateTimeField()
	name 	=	models.CharField(max_length=250)
	dec 	=	models.TextField()
	value 	=	models.IntegerField()
	class Meta:
		db_table	=	'e_expenses'
	def __str__(self):
		return " %s | %s | %s "%(self.name, self.dec, self.value)

class Ecourse(models.Model):
	name 	=	models.CharField(max_length=250)
	class Meta:
		db_table	=	'e_course'
	def __str__(self):
		return self.name

class Estudent(models.Model):
	name 	=	models.CharField(max_length=250)
	address	=	models.TextField()
	phone	=	models.CharField(max_length=13)
	email	=	models.CharField(max_length=250)
	class Meta:
		db_table	=	'e_student'
	def __str__(self):
		return "%s | %s"%(self.name, self.phone)

class Eenquiry(models.Model):
	name 		=	models.CharField(max_length=250)
	course 		=	models.ForeignKey(Ecourse)
	student 	=	models.ForeignKey(Estudent)
	class Meta:
		db_table	=	'e_enquiry'
	def __str__(self):
		return "%s | %s | %s"%(self.name, self.student, self.course)

