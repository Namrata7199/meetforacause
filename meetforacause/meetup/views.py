# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import EventForm
from .models import Event
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
import urllib.request, json


# Create your views here.


def home(request):
    events_list = Event.objects.all()
    return render(request, 'home.html', {'list': events_list})


@login_required
def add(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            x = form.save(commit=False)
            x.organiser = request.user
            key = 'AIzaSyAxBislywSht1-OINIsHfCmsYpU4N7wvJw'
            url = ('https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
                   '?input=%s'
                   '&inputtype=textquery'
                   '&fields=formatted_address,name,geometry'
                   '&key=%s') % (x.street, key)
            response = urllib.request.urlopen(url)
            json_raw = response.read()
            json_data = json.loads(json_raw)
            print(json_data)
            x.latitude = json_data['candidates'][0]['geometry']['location']['lat']
            x.longitude = json_data['candidates'][0]['geometry']['location']['lng']
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


def search_by_location(request):
    if request.method == "POST":
        location = request.POST['location']
        if location:
            events = Event.objects.filter(city=location)
            if events:
                return render(request, 'home.html', {'list': events})
            else:
                return render(request, 'home.html', {'error_message': "No events found for this location"})
        else:
            return redirect('home')
    else:
        return redirect('home')


def event_details(request, pk):
    detail = Event.objects.get(pk=pk)
    return render(request, 'event_details.html', {'detail': detail})


@login_required
def attend(request, pk):
    meet = Event.objects.get(pk=pk)
    user = request.user
    meet.attendees.add(user)
    return render(request, 'thanks.html')


@login_required
def organise(request, pk):
    meet = Event.objects.get(pk=pk)
    user = request.user
    meet.group.add(user)
    # return render(request, 'thanks.html')
    return render(request, 'sponsor.html', {'meet': meet})


@login_required
def sponsor(request, pk):
    meet = Event.objects.get(pk=pk)
    user = request.user
    meet.sponsors.add(user)
    return render(request, 'sponsor.html', {'meet': meet})


@login_required
def paid_services(request, pk):
    event = Event.objects.get(pk=pk)
    return render(request, 'paid_services.html', {'event': event})
