from django.contrib import admin
from django.urls import path
from . import views


app_name = 'contact_about'

urlpatterns = [
     path('', views.contact_about, name='contact_about'),
]
