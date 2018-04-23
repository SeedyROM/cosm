from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth import authenticate
from rest_framework import status

from core.testing import APITestCase


class TestAuthentication(APITestCase):
    @classmethod
    def setUpClass(klass):
        super().setUpClass()

        klass.obtain_token_url = reverse('authentication:obtain_jwt_token')
        klass.user_data = {'username': 'admin', 'password': 'password123'}
        klass.user = get_user_model().objects.create_user(**klass.user_data)

    def test_obtain_token_fails_with_invalid_info(self):
        bad_data = {'username': 'tfasfesdsajkfjslkat', 'password': 'passdashfkjawwo'}
        resp = self.client.post(self.obtain_token_url, bad_data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_obtain_token_with_valid_info(self):
        resp = self.client.post(self.obtain_token_url, self.user_data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)