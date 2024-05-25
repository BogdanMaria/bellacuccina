from django.contrib import admin
from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('products/', views.store_products, name='store_products'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),

]