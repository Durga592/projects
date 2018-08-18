# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Appdetails(models.Model):
	name 	=	models.CharField(max_length=255)

class Customerdetails(models.Model):
	name 	=	models.CharField(max_length=255)