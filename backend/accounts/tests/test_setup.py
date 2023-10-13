from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse("user-registration")

        self.user_data = {
            "email": "fake_user@example.com",
            "username": "fake_user",
            "first_name": "John",
            "last_name": "Doe",
            "password": "A v3ry d1fficult p@$$w0rD!",
        }
