from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from .models import Order, OrderLineItem
from customer_profile.models import CustomerProfile
from products.models import Category, Product


class TestOrderModel(TestCase):

    @classmethod
    def setUp(self):
        """
        creating and saving a new test user
        """
        self.user = User.objects.create(
            username='MyTestUser',
            password='mypass79',
            email='test@user.com',
            id='1',
        )
        self.user.save()

        self.customer_profile = CustomerProfile.objects.get(user=self.user)

        self.my_order = Order.objects.create(
                order_number='8D69DEBED9F84672B3B457EB841E1C0D',
                user_profile=self.customer_profile,
                full_name='Test User',
                email='test@user.com',
                phone_number='123445',
                country='Croatia',
                postcode='P12WER',
                town_or_city='Zagreb',
                street_address1='Somwhere',
                street_address2='Somwhere near 2',
                county='Zagorje',
                date='2024-06-27T12:00:00',
                order_total='230.50',
                grand_total='230.50',
                original_cart='Cart',
                stripe_pid='p18'
                )

    def teardown(self):
        self.my_order.delete()
        self.customer_profile.delete()
        self.user.delete()

    def test_order_creation(self):
        self.assertTrue(Order.objects.filter(order_number='8D69DEBED9F84672B3B457EB841E1C0D'))
        self.assertEqual(str(self.my_order), '8D69DEBED9F84672B3B457EB841E1C0D')

    def test_generate_order_number(self):
        self.assertTrue(self.my_order._generate_order_number())


class TestOrderLineItemModel(TestCase):

    @classmethod
    def setUp(self):
        """
        creating and saving a new test user, product, and order
        """
        self.user = User.objects.create(
            username='MyTestUser',
            password='mypass79',
            email='test@user.com',
            id='1',
        )
        self.user.save()

        self.customer_profile = CustomerProfile.objects.get(user=self.user)

        self.my_category = Category.objects.create(
            name='Pasta',
            notes='test notes',
            slug='testslug',
            friendly_name='Pasta'
        )
        self.my_category.save()
        self.product = Product.objects.create(
            category=self.my_category,
            item_no='A221',
            name='Pasta',
            description='Test pasta description',
            price=5.00,
            weight=500,

        )

        self.my_order = Order.objects.create(
                order_number='8D69DEBED9F84672B3B457EB841E1C0D',
                user_profile=self.customer_profile,
                full_name='Test User',
                email='test@user.com',
                phone_number='123445',
                country='Croatia',
                postcode='P12WER',
                town_or_city='Zagreb',
                street_address1='Somwhere',
                street_address2='Somwhere near 2',
                county='Zagorje',
                date='2024-06-27T12:00:00',
                order_total='230.50',
                grand_total='230.50',
                original_cart='Cart',
                stripe_pid='p18'
                )
        self.new_oderlineitem = OrderLineItem.objects.create(
            order=self.my_order,
            product=self.product,
            quantity=2,
            lineitem_total=461.00
        )
        self.new_oderlineitem.save()

    def test_orderlineitem_creation(self):
        self.assertEqual(OrderLineItem.objects.count(), 1)
        self.assertEqual(str(self.new_oderlineitem),f'ITEM_NO {self.product.item_no} on order {self.my_order.order_number}')