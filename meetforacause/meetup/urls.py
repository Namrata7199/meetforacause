from django.urls import path, include
from . import views
from django.contrib import admin

admin.site.site_header = 'Meet Up Admin'

urlpatterns = [
    path('home/', views.home, name='home'),
]