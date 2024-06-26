from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_content(request):

    cart_items = []
    total = 0
    all_items = 0
    product = None
    cart_data = request.session.get('cart', {})
    for product_id, cart_item in cart_data.items():
        if isinstance(cart_item['qty'], int):
            product = get_object_or_404(Product, pk=product_id)

            total += int(cart_item['qty']) * float(cart_item['price'])
            cart_items.append({
                'item_id': product_id,
                'product': product,
                'quantity': cart_item['qty'],

            })

    all_items = sum(cart_item['qty'] for cart_item in cart_data.values())
    context = {
        'cart_data': cart_data,
        'total': total,
        'total_items': len(cart_data),
        'cart_items': cart_items,
        'my_product': product,
        'all_items': all_items,
    }

    return context


def my_cart(request):
    current_cart = request.session.get('cart', {})
    return {'current_cart': current_cart}
