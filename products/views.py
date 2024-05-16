from django.shortcuts import render


def store_products(request):
    template = 'products/store_products.html'
    context = {}
    return render(request, template, context)