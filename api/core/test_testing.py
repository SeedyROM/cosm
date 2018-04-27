from core.testing import APITestCase

class TestAPITestCase(APITestCase):
    def test_tests(self):
        self.assertTrue(hasattr(self, 'pytestmark'))
        self.assertTrue(hasattr(self, 'mixer'))
        