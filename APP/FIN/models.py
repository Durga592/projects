# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.conf import settings

from django.contrib.sessions.models import Session


# Create your models here.
class Emp(models.Model):
	name=models.CharField(max_length=250)
	sala=models.IntegerField()
	age=models.IntegerField()
	
class Userdets(models.Model):
	name		=	models.CharField("USER FULL NAME", max_length=250)
	username	=	models.CharField("USER LOGIN NAME", max_length=250)
	password	=	models.CharField("USER PASSWORD", max_length=250)
	mailid		=	models.CharField("USER MAIL ID", max_length=250)
	
class UserSession(models.Model):
    user 		= 	models.ForeignKey(settings.AUTH_USER_MODEL)
    session 	= 	models.ForeignKey(Session)