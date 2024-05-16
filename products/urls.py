from django.contrib import admin
from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('products/', views.store_products, name='store_products'),

]