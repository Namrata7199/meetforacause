from django.urls import path, include
from . import views
from django.contrib import admin

admin.site.site_header = 'Meet Up Admin'

urlpatterns = [
    path('', views.home, name='home'),
    path('add',views.add, name='add'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/login_user', views.login_user, name='login_user'),
    path('events/<int:pk>',views.event_details, name="event_details"),
    path('events/<int:pk>/attend',views.attend,name="attend"),
]