from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from profiles.models import Profile
from dependencies.models import Gender, Language, Status
from django.urls import reverse


# Create your tests here.
class ApplicationTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.application_route = reverse("applications-list")

        user = User.objects.create(username="test")
        user.set_password("1235678")
        user.save()
        self.user = user

        self.gender = Gender.objects.create(gender="Male")
        self.language = Language.objects.create(language="English")
        self.status = Status.objects.create(status="Saved")
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
            # TODO: refactor to be a CharField / Enum
            "recruiter_gender": self.gender.pk,
            "application_language": self.language.pk,
            # TODO: refactor to be a CharField / Enum
            "status": self.status.pk,  # I don't like this having to be in a table -- it can be a CharField / Enum
        }

        self.token = Token.objects.create(user=self.user)
        self.token_header = f"Token {self.token.key}"

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

        self.assertEqual(res.data["profile"], self.APPLICATION_DATA["profile"])

    # TODO
    # - add test for DELETE
    # - add test for PUT
    # - add test for GET (single application)
    # - add test for GET (list of applications)
