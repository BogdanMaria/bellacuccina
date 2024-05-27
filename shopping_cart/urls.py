from django.contrib import admin
from django.urls import path


from . import views


app_name = 'shopping_cart'

urlpatterns = [
    path('cart/', views.cart, name='cart'),
]