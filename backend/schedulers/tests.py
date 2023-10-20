from rest_framework.test import APITestCase, APIClient
from .models import Scheduler
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from applications.models import Application
from profiles.models import Profile
from dependencies.models import Language
from django.utils import timezone
import datetime
from django.urls import reverse


# Create your tests here.
class SchedulerTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.schedule_route = reverse("scheduler-list")

        self.user = User.objects.create(username="test", password="123")
        self.gender = "Male"
        self.language = Language.objects.create(language="English")
        self.status = "Saved"
        self.profile = Profile.objects.create(user=self.user, gender=self.gender)
        self.application = Application.objects.create(
            profile=self.profile,
            position="front",
            company="test",
            description="test",
            company_email="test@test.com",
            application_language=self.language,
            status=self.status,
            recruiter_gender=self.gender,
        )

        self.scheduler_data = {
            "interview_shedule": "2023-10-18T15:29:43.477Z",
            "interview_time_before": "14:00:00",
            "interview_time_after": "16:00:00",
            "user": self.user.pk,
            "application": self.application.pk,
        }

        self.token = Token.objects.create(user=self.user)
        self.token_header = f"Token {self.token.key}"

    def test_scheduler_cannot_create_with_no_data(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.token_header)
        res = self.client.post(self.schedule_route)
        self.assertEqual(res.status_code, 400)

    def test_scheduler_post(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.token_header)
        res = self.client.post(self.schedule_route, self.scheduler_data, format="json")

        self.assertEqual(res.status_code, 201)
        # always confirm with some real data
        copy_of_response = res.data.copy()
        del copy_of_response["id"]
        self.assertDictEqual(
            copy_of_response,
            {
                "interview_shedule": "2023-10-18T17:29:43.477000+02:00",
                "interview_time_before": "14:00:00",
                "interview_time_after": "16:00:00",
                "user": self.user.pk,
                "application": self.application.pk,
            },
        )

    def test_scheduler_creation(self):
        # unit test
        time_saved = timezone.now()
        time_before = time_saved - datetime.timedelta(hours=1)
        time_after = time_saved + datetime.timedelta(hours=1)
        scheduler = Scheduler.objects.create(
            user=self.user,
            application=self.application,
            interview_shedule=time_saved,
            interview_time_before=time_before,
            interview_time_after=time_after,
        )
        self.assertEqual(time_saved, scheduler.interview_shedule)
