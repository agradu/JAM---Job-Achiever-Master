from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from simulations.models import Simulation
from applications.models import Application
from profiles.models import Profile
from dependencies.models import Language
from django.urls import reverse
from datetime import datetime

# Create your tests here.
class SimulationTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.simulation_route = reverse("simulations-list")

        self.user = User.objects.create(username="test")
        self.user.set_password("1235678")
        self.user.save()
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
        self.SIMULATION_DATA = {
            "user": self.user.pk,
            "application": self.application.pk,
            "recruiter_attitude": "normal",
            "language": self.language.pk,
            "json_file": [{"role": "user", "content": "Just a test."}],
            "review": "A test review.",
            "created_at": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        }

        self.token = Token.objects.create(user=self.user)
        self.token_header = f"Token {self.token.key}"

    def test_simulation_cannot_create_with_no_data(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.token_header)
        res = self.client.post(self.simulation_route)
        self.assertEqual(res.status_code, 400)

    def test_simulation_post(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.token_header)
        res = self.client.post(
            self.simulation_route, self.SIMULATION_DATA, format="json"
        )
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data["user"], self.SIMULATION_DATA["user"])
        self.assertEqual(res.data["application"], self.SIMULATION_DATA["application"])
        self.assertEqual(res.data["language"], self.SIMULATION_DATA["language"])
        self.assertEqual(res.data["json_file"], self.SIMULATION_DATA["json_file"])
        self.assertEqual(res.data["review"], self.SIMULATION_DATA["review"])
        self.assertEqual(res.data["created_at"][:19], self.SIMULATION_DATA["created_at"][:19])

    # TODO
    # - add test for DELETE
    # - add test for PUT
    # - add test for GET (single application)
    # - add test for GET (list of applications)