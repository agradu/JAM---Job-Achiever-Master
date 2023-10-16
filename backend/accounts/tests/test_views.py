from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestViews(APITestCase):
    def setUp(self):
        self.register_url = reverse("user-registration")

        self.user_data = {
            "email": "fake_user@example.com",
            "username": "fake_user",
            "first_name": "John",
            "last_name": "Doe",
            "password": "A v3ry d1fficult p@$$w0rD!",
        }

    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_user_can_register_correctly(self):
        res = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(res.data["user_id"], 1)
        self.assertEqual(res.status_code, 201)

    def test_user_login(self):
        user = User(**self.user_data)
        user.set_password(user.password)
        user.save()
        res = self.client.post(reverse("rest_login"), self.user_data, format="json")
        self.assertEqual(res.status_code, 200)
        # check for Token (also known as key)
        self.assertTrue("key" in res.data)

    def test_user_login_fail(self):
        res = self.client.post(
            reverse("rest_login"),
            {"username": "doesnotexist", "password": "password"},
            format="json",
        )
        self.assertEqual(res.status_code, 400)
        self.assertDictEqual(
            res.json(),
            {"non_field_errors": ["Unable to log in with provided credentials."]},
        )
