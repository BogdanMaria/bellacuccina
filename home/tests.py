from django.test import TestCase, Client
from django.urls import reverse, resolve

# Create your tests here.
class TestHomeView(TestCase):

    def test_home_page_loads(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)