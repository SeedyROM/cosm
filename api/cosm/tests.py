from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from unittest import TestCase

from core.testing import APITestCase
from . import urls


class TestAccountsIntegration(APITestCase):
    @classmethod
    def setUpClass(klass):
        super().setUpClass()
        
        klass.register_url = reverse('rest_registration:register')
        klass.user_data = {
            'username': 'bob',
            'password': 'password123',
            'password_confirm': 'password123',
        }
        
    def test_register(self):
        resp = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

class TestReducedRegisterUrls(TestCase):
    def test_remove_login_and_logout(self):
        url_list, namespace = urls.reducedRegistrationRoutes()
        self.assertEqual(namespace, 'rest_registration')

        for url in url_list:
            self.assertNotIn(url.name, ['login', 'logout'])