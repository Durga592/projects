# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class StudyHall(models.Model):
	name	=	models.CharField(max_length=100)
	area	=	models.TextField(max_length=250)

	class Meta:
		db_table	=	'study_hall'

class NewCourse(models.Model):
	name		=	models.CharField(max_length=250)
	class Meta:
		db_table	=	'course' 

class Student(models.Model):
	name	=	models.CharField(max_length=250)
	address	=	models.TextField(max_length=250)
	phone	=	models.CharField(max_length=13)
	email	=	models.CharField(max_length=250)

	class Meta:
		db_table	=	'student'

class Enquiry(models.Model):
	name	=	models.CharField(max_length=250)
	course 	=	models.ForeignKey(NewCourse)	
	student =	models.ForeignKey(Student)	
	
	class Meta:
		db_table	=	'enquiry'

class Expense(models.Model):
	study_hall	=	models.ForeignKey(StudyHall)
	name		=	models.CharField(max_length=250)
	date 		=	models.DateField()
	doc_no		=	models.CharField(max_length=100)
	amount		=	models.IntegerField()
	description	=	models.TextField()

	class Meta:
		db_table	=	'expense'
