from django.shortcuts import render

from .models import Product


def store_products(request):

    products = Product.objects.all()
    template = 'products/store_products.html'
    context = {
        'products': products,
    }
    
    return render(request, template, context)