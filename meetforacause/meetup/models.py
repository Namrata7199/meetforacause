# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class event(models.Model):
	title = models.CharField(max_length=100)
	cause = models.CharField(max_length=1000)
	image = models.ImageField(upload_to='media/')
	organiser = models.OneToOneField(User, related_name="organiser", on_delete=models.CASCADE)
	attendees = models.ManyToManyField(User, related_name="atendees")
	non_attendees = models.ManyToManyField(User, related_name="non_attendees")
	city = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	date = models.DateField()
	time = models.TimeField()

