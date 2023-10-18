from rest_framework.test import APITestCase
from django.urls import reverse
from schedulers.models import Scheduler


class TestSchedulerViews(APITestCase):
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
            "time_saved": "18.10.2023 12:00:00",
            "time_before": "18.10.2023 11:00:00",
            "time_after": "18.10.2023 13:00:00",
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
        scheduler = Scheduler(**self.scheduler_data)
        scheduler.save()
        res = self.client.post(self.register_url, self.scheduler_data, format="json")
        self.assertEqual(res.status_code, 201)