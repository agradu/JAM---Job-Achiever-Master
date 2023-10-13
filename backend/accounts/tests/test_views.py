from django.test import TestCase
from .test_setup import TestSetUp
from django.contrib.auth.models import User

# Create your tests here.

class TestViews(TestSetUp):
    def test_user_cannot_register_with_no_data(self):
        res =  self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)
    
    def test_user_can_register_correctly(self):
        res =  self.client.post(
            self.register_url, self.user_data, format="json")
        self.assertEqual(res.data['user_id'], 1)
        self.assertEqual(res.status_code, 201)
        
    def test_user_cannot_login_with_unverified_email(self):
        res =  self.client.post(
            self.register_url, self.user_data, format="json")
        breakpoint()
        res = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 401)
    
    def test_user_cannot_login_after_verification(self):
        response = self.client.post(
            self.register_url, self.user_data, format="json")
        self.assertEqual(response.status_code, 201)  # Check for a successful registration

        user_id = response.data.get('user_id')
        self.assertIsNotNone(user_id)

        # Retrieve the user by user_id and update the is_verified flag
        user = User.objects.get(id=user_id)
        user.is_verified = True
        user.save()
        user.refresh_from_db()  # Refresh the user object from the database

        # Attempt to log in
        login_response = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(login_response.status_code, 200)  # Check for successful login after verification
