from django.test import TestCase, Client
from django.urls import reverse, resolve

from .models import Wishlist
from products.models import Product, Category
from django.contrib.auth.models import User


class TestWishlistModel(TestCase):

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

    def tearDown(self):
        self.user.delete()

    def test_string_method_return(self):
        self.my_wishlist = Wishlist.objects.create(
            user=self.user,
            product=self.product

        )
        self.assertEqual(str(self.my_wishlist), 'Pasta in Pasta')
