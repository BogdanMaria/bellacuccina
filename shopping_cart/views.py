from django.shortcuts import render


def cart(request):
    """
    view to render the shopping cart
    """
    template = 'shopping_cart/cart.html'
    # context = {}
    return render(request, template)
