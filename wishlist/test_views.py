from django.test import TestCase, Client
from django.urls import reverse, resolve

from .models import Wishlist
from products.models import Product, Category
from django.contrib.auth.models import User


class TestWishlistView(TestCase):

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
        self.user.set_password('mypass799')
        self.user.save()

        self.my_category = Category.objects.create(
            name='Savage',
            notes='test notes',
            slug='testslug',
            friendly_name='Pasta'
        )
        self.my_category.save()

        self.product = Product.objects.create(
            category=self.my_category,
            item_no='A221',
            name='Test pasta',
            description='Test pasta description',
            price=5.00,
            weight=500,
        )

    def tearDown(self):
        self.my_category.delete()
        self.product.delete()
        self.user.delete()

    def test_rendering_right_template(self):
        """
        anonymous user trying to access wishlist view
        redirected to login
        """
        response = self.client.get('/wishlist/')
        self.assertEqual(response.status_code, 302)

        """
        logged in user accessing wishlist view
        """

        self.client.login(username='MyTestUser', password='mypass799')
        response = self.client.get('/wishlist/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wishlist/wishlist.html')


class TestAddingToWishlist(TestCase):

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
        self.user.set_password('mypass799')
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
            name='Test Pasta',
            description='Test pasta description',
            price=5.00,
            weight=500,
            id=23,
        )
        self.product.save()

    def test_add_to_wishlist(self):
        self.client = Client()
        self.client.force_login(self.user)
        self.redirect_url = reverse(('products:store_products'))
        response = self.client.post('/wishlist/add_to_wishlist/', data={
            'product-id': self.product.id,
            'my_redirect_url': self.redirect_url

        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Wishlist.objects.count(), 1)
        self.assertRedirects(response, reverse('products:store_products'))



class TestRemovingFromWishlist(TestCase):

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
        self.user.set_password('mypass799')
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
            id=23,
        )
        self.product.save()

    def test_removing_from_wishlist(self):
        self.client = Client()
        self.client.force_login(self.user)
        wishlist_item = Wishlist.objects.create(user=self.user, product_id=23)
        wishlist_item_id = wishlist_item.id
        response = self.client.post('/wishlist/remove_from_wishlist/', data={'item-id': wishlist_item_id})
        print(f"Wishlist count: {Wishlist.objects.count()}")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Wishlist.objects.count(), 0)