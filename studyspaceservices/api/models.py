# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Ehall(models.Model):
	name	=	models.CharField(max_length=250)
	area	=	models.TextField()
	hall_status	=	models.IntegerField(default = 1, help_text = " 1 - active, 0 - de_active")
	class Meta:
		db_table	=	'e_hall'
	def __str__(self):
		return "%s | %s"%(self.name, self.area)

class Eexpenses(models.Model):
	ehall 	=	models.ForeignKey(Ehall)
	date 	=	models.DateTimeField(blank=True, null=True)
	name 	=	models.CharField(max_length=250)
	dec 	=	models.TextField(blank=True, null=True)
	value 	=	models.IntegerField()
	exp_status	=	models.IntegerField(default = 1, help_text = " 1 - active, 0 - de_active")
	class Meta:
		db_table	=	'e_expenses'
	def __str__(self):
		return " %s | %s | %s "%(self.name, self.dec, self.value)

class Ecourse(models.Model):
	name 	=	models.CharField(max_length=250)
	course_status	=	models.IntegerField(default = 1, help_text = " 1 - active, 0 - de_active")
	class Meta:
		db_table	=	'e_course'
	def __str__(self):
		return self.name

class Estudent(models.Model):
	name 	=	models.CharField(max_length=250)
	address	=	models.TextField()
	phone	=	models.CharField(max_length=13)
	email	=	models.CharField(max_length=250)
	student_status	=	models.IntegerField(default = 1, help_text = " 1 - active, 0 - de_active")
	class Meta:
		db_table	=	'e_student'
	def __str__(self):
		return "%s | %s"%(self.name, self.phone)

class Eenquiry(models.Model):
	name 		=	models.CharField(max_length=250)
	course 		=	models.ForeignKey(Ecourse)
	student 	=	models.ForeignKey(Estudent)
	enquiry_status	=	models.IntegerField(default = 1, help_text = " 1 - active, 0 - de_active")
	class Meta:
		db_table	=	'e_enquiry'
	def __str__(self):
		return "%s | %s | %s"%(self.name, self.student, self.course)
class New(models.Model):
	ehall 	=	models.ForeignKey(Ehall)	
	name 	=	models.CharField(max_length=250)