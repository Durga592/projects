# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from django.contrib.auth.models import	User

# Create your models here.
########## FILE UPLOADING #######################################
class Document(models.Model):
	description =	models.CharField(max_length=255, blank=True)
	document 	=	models.FileField(upload_to='documents/')
	uploaded_at	=	models.DateTimeField(auto_now_add=True)