from django.test import TestCase, Client
from django.urls import reverse
from bella_cuccina import urls
from .views import handler500, handler403


class TestHandlerViews(TestCase):
    def test_404_error(self):
        response = self.client.get('/re')
        self.assertEqual(response.status_code, 404)
