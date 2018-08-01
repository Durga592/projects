# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contacts(models.Model):
	full_name	=	models.CharField(max_length=255)
	number		=	models.CharField(max_length=255)