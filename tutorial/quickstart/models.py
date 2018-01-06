# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Song(models.Model):
	name = models.CharField(max_length=45)
	duration = models.CharField(max_length=45)
	
	def __str__(self):
		return self.name
		
class Employee(models.Model):
	name = models.CharField(max_length=45)
	position = models.CharField(max_length=45)
	
	def __str__(self):
		return self.name