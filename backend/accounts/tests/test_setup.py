from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetUp(APITestCase):
    
    def setUp(self):
        self.register_url = reverse("user-registration")
        self.login_url = reverse("user-login")
        
        self.user_data={
            "username":"fake_user",
            "email": "fake_user@example.com",
            "password":"A v3ry d1fficult p@$$w0rD!"
        }
        
        return super().setUp()

    def tearDpwn(self):
        return super().tearDown()