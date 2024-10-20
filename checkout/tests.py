from django.test import TestCase

from .models import Order, OrderLineItem
from customer_profile.models import CustomerProfile
from products.models import Product


class TestOrderModel(TestCase):
    """
    creating a test order
    """

    def test_string_method_return_order_num(self):
        new_order = Order.objects.create(
            order_number='A7AEF9E2B7E44986BEB538E58EE25BBE',
            full_name='Test user',
            email='test@bo.com',
            phone_number='353231245',
            country='Ireland',
            postcode='P12RE44',
            street_address1='Sowhere',
            street_address2='Sowhere2',
            county='Laois',
            date='12.05.2023',
            order_total='220.00',
            grand_total='220.00',
            original_cart='',
            stripe_pid='12we'

        )
        self.assertEqual(str(new_order), 'A7AEF9E2B7E44986BEB538E58EE25BBE')
