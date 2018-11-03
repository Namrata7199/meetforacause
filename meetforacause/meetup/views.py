# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import EventForm
from django.shortcuts import render,redirect

# Create your views here.


def home(request):
    return render(request, 'base.html')

def add(request):
	if request.method=='POST':
		form = EventForm(request.POST,request.FILES)
		if form.is_valid():
			x = form.save(commit=False)
			#x.organiser = request.user
			#x.save()
			return redirect('home')
	else:
		form = EventForm()
	return render(request,'add_event.html',{'form' : form})

