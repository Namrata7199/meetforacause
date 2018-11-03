from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Event

class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ['title', 'cause', 'city', 'country', 'date', 'time', 'image',]