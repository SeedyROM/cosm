import pytest
from rest_framework.test import APITestCase as RestFrameworkApiTestCase
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db

@pytest.mark.django_db
class APITestCase(RestFrameworkApiTestCase):
    pytestmark = pytest.mark.django_db
    mixer = mixer