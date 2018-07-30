# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Document(models.Model):
	description =	models.CharField(max_length=255, blank=True)
	document 	=	models.FileField(upload_to='documents/')
	uploaded_at	=	models.DateTimeField(auto_now_add=True)
	#created		=	models.ForeignKey(User)

class Studyhall(models.Model):
	name		=	models.CharField(max_length=255)
	area		=	models.TextField()
	hall_status	=	models.IntegerField(default = 1, help_text = " 1 - active, 0 - de_active")
	created_at	=	models.DateTimeField(blank=True, null=True, )
	created 	=	models.ForeignKey(User, blank=True, null=True, related_name = '%(class)s_requests_created')
	updated_at	=	models.DateTimeField(blank=True, null=True, )
	updated 	=	models.ForeignKey(User, blank=True, null=True, related_name = '%(class)s_requests_updated')
	atrribute1	=	models.IntegerField(blank=True, null=True)
	atrribute2	=	models.IntegerField(blank=True, null=True)
	atrribute3	=	models.IntegerField(blank=True, null=True)
	atrribute4	=	models.CharField(max_length=255, blank=True, null=True)
	atrribute5	=	models.CharField(max_length=255, blank=True, null=True)
	atrribute6	=	models.CharField(max_length=255, blank=True, null=True)
	doc_name	=	models.FileField(upload_to='uploads/')