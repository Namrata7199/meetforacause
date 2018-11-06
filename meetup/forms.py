from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'cause', 'street', 'city', 'date', 'time', 'image', 'summary', ]


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

# class SponsorForm(ModelForm):
# 	class Meta:
# 		model : sponsor_details
# 		fields = ['name','email','contact_no',]
