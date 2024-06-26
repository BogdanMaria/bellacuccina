from django.contrib import admin
from django.urls import path

from . import views


app_name = 'wishlist'

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('add_to_wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('wishlist_total/', views.wishlist_total, name='wishlist_total'),
]
