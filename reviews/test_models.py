from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from .models import Review
from products.models import Category, Product


class TestReviewModel(TestCase):

    @classmethod
    def setUp(self):
        """
        creating and saving a new test review
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

        self.my_review = Review.objects.create(
            author=self.user,
            product=self.product,
            content='My test review'

        )

    def tearDown(self):
        self.my_review.delete()
        self.my_category.delete()
        self.product.delete()
        self.user.delete()

    def test_string_method_return(self):
        self.assertEqual(str(self.my_review),
                         'Review by MyTestUser for Test Pasta: My test review'

                         )