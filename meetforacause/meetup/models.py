# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=100)
    cause = models.CharField(max_length=1000)
    image = models.ImageField()
    organiser = models.ForeignKey(User, related_name="organiser", on_delete=models.CASCADE, blank=True)
    group = models.ManyToManyField(User, related_name="group", blank=True)
    attendees = models.ManyToManyField(User, related_name="attendees", blank=True)
    sponsors = models.ManyToManyField(User, related_name="non_attendees", blank=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    summary = models.TextField()

