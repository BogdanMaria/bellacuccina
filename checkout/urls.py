from django.contrib import admin
from django.urls import path

from . import views


app_name = 'checkout'

urlpatterns = [
    path('checkout/', views.store_checkout, name='store_checkout')


]