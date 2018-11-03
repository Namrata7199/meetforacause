# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import EventForm
from django.shortcuts import render,redirect
from .models import Event
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
	list = Event.objects.all()
	return render(request, 'home.html',{'list' : list})


@login_required
def add(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            x = form.save(commit=False)
            x.organiser = request.user
            x.save()
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')  # , pk=user.security.id)
            else:
                return render(request, 'login_user.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login_user.html', {'error_message': 'Invalid login'})
    return render(request, 'login_user.html')

def event_details(request, pk):
	detail = Event.objects.get(pk=pk)
	return render(request,'event_details.html',{'detail' : detail})
