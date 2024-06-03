from django.contrib import admin
from django.urls import path

from . import views


app_name = 'wishlist'

urlpatterns = [
    path('', views.wishlist, name='wishlist '),
    path('add_to_wishlist/', views.add_to_wishlist, name='add_to_wishlist'),

]