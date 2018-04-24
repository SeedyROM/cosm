from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

from core.testing import APITestCase


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
        print(resp.data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
