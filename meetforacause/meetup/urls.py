from django.urls import path, include
from . import views
from django.contrib import admin

admin.site.site_header = 'Meet Up Admin'

urlpatterns = [
    path('', views.home, name='home'),
    path('add',views.add, name='add'),
]