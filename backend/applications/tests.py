from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from profiles.models import Profile
from dependencies.models import Language
from django.urls import reverse
from .models import Application


# Create your tests here.
class ApplicationTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.application_route = reverse("applications-list")

        user = User.objects.create(username="test")
        user.set_password("1235678")
        user.save()
        self.user = user

        self.gender ="male"
        self.language = Language.objects.create(language="English")
        self.profile = Profile.objects.create(user=self.user, gender=self.gender)

        self.APPLICATION_DATA = {
            "position": "CEO",
            "company": "string",
            "description": "string",
            "cover_letter_text": "string",
            "cv_short_description": "string",
            "company_email": "user@example.com",
            "company_address": "string",
            "source": "string",
            "recruiter_name": "string",
            "recruiter_position": "string",
            "status_date": "2023-10-18T19:41:11.619Z",
            "profile": self.profile.pk,
            "recruiter_gender": self.gender,
            "application_language": self.language.pk,
            "status": "Saved",
        }

        self.token = Token.objects.create(user=self.user)
        self.token_header = f"Token {self.token.key}"

    def test_application_get_all(self):
        Application.objects.create(
            profile=self.profile,
            position="front",
            company="test",
            description="test",
            company_email="test@test.com",
            application_language=self.language,
            recruiter_gender=self.gender,
        )
        self.client.credentials(HTTP_AUTHORIZATION=self.token_header)
        res = self.client.get(self.application_route)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data.get("results", [])), 1)

    def test_application_get_all_when_not_owner(self):
        user = User.objects.create(username="test2")
        profile = Profile.objects.create(user=user, gender=self.gender)
        Application.objects.create(
            profile=profile,
            position="front",
            company="test",
            description="test",
            company_email="test@test.com",
            application_language=self.language,
            recruiter_gender=self.gender,
        )
        self.client.credentials(HTTP_AUTHORIZATION=self.token_header)
        res = self.client.get(self.application_route)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data.get("results", [])), 0)

    def test_application_post(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.token_header)
        res = self.client.post(
            self.application_route, self.APPLICATION_DATA, format="json"
        )
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data["position"], self.APPLICATION_DATA["position"])
        self.assertEqual(res.data["company"], self.APPLICATION_DATA["company"])
        self.assertEqual(res.data["description"], self.APPLICATION_DATA["description"])
        self.assertEqual(
            res.data["cover_letter_text"], self.APPLICATION_DATA["cover_letter_text"]
        )
        self.assertEqual(
            res.data["cv_short_description"],
            self.APPLICATION_DATA["cv_short_description"],
        )
        self.assertEqual(
            res.data["company_email"], self.APPLICATION_DATA["company_email"]
        )

        self.assertEqual(
            res.data["company_address"], self.APPLICATION_DATA["company_address"]
        )

        self.assertEqual(res.data["source"], self.APPLICATION_DATA["source"])
        self.assertEqual(
            res.data["recruiter_name"], self.APPLICATION_DATA["recruiter_name"]
        )
        self.assertEqual(
            res.data["recruiter_position"], self.APPLICATION_DATA["recruiter_position"]
        )
        # TODO: Handle dates because of a seconds difference
        # self.assertEqual(
        #     res.data["status_date"], self.APPLICATION_DATA["status_date"]
        # )
        # expected_status_date_str = "2023-10-18T19:41:11.619Z"
        # actual_status_date_str = res.data["status_date"]
        # expected_status_date = datetime.fromisoformat(expected_status_date_str)
        # actual_status_date = datetime.fromisoformat(actual_status_date_str)
        # time_tolerance = timedelta(seconds=10)  # 1 second tolerance

        # # Check if the time difference is within the acceptable tolerance
        # self.assertLessEqual(abs(expected_status_date - actual_status_date), time_tolerance)

    # TODO
    # @Victor this doesn't work, I think because View Logic doesn't have methods for PUT, GET, DELETE

    
    # - add test for DELETE
    # def test_application_delete(self):
    #     self.client.credentials(HTTP_AUTHORIZATION=self.token_header)
    #     res = self.client.delete(self.application_route)
    #     self.assertEqual(res.status_code, 204)
    # - add test for PUT
    # - add test for GET (single application)
    # - add test for GET (list of applications)
