from django.test import TestCase, RequestFactory
from django.urls import reverse
from .views import post_list


class MyViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.resource = reverse('post_list')

    def test_get(self):
        request = self.factory.get(self.resource)
        response = post_list(request)
        self.assertEqual(response.status_code, 200)

