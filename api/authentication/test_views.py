from django.urls import reverse
from rest_framework import status
from core.testing import APITestCase

class TestAuthentication(APITestCase):
    def test_obtain_token(self):
        url = reverse('authentcation:obtain_token')
        