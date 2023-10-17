from rest_framework.test import APITestCase
from django.urls import reverse
import datetime


class TestViews(APITestCase):
    def setUp(self):
        self.register_url = reverse("scheduler")

        self.scheduler_data = {
            "user_email": "fake_user@example.com",
            "username": "fake_user",
            "first_name": "John",
            "last_name": "Doe",
            "password": "A v3ry d1fficult p@$$w0rD!",
            "user_languade": "English",
            "user_gender": "Male",
            "user_status": "Saved",
            "time_saved": datetime.datetime.now(),
            "time_before": datetime.datetime.now() - datetime.timedelta(hours=1),
            "time_after": datetime.datetime.now() + datetime.timedelta(hours=1),
            "position": "front", 
            "company":"test", 
            "description":"test", 
            "company_email":"test@test.com",
            "application_language":"English", 
            "status":"Apply", 
            "recruiter_gender":"Male"
        }

    def test_scheduler_cannot_create_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_scheduler_creation(self):
        res = self.client.post(self.register_url, self.scheduler_data, format="json")
        self.assertEqual(res.status_code, 201)