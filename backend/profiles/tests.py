from rest_framework.test import APITestCase, APIClient
from .models import Profile, Education, Experience, ProfileSkill, ProfileHobby, ProfileLanguage
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from dependencies.models import Language
from django.urls import reverse

# Create your tests here.
class ProfileTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.profile_route = reverse("profile-list")

        self.user = User.objects.create(username="semen", password="123")
        self.gender = "male"
        self.language = Language.objects.create(language="English")
        self.status = "Saved"
        self.profile = Profile.objects.create(user=self.user, gender=self.gender, birthday="2000-10-18")
        self.education = Education.objects.create(profile=self.profile, title="education title", start_date="2020-10-18", end_date="2023-10-18")
        self.experience = Experience.objects.create(profile=self.profile, title="experience title", company="company title", description="company description", start_date="2020-10-18", end_date="2023-10-18")
        self.profile_skill = ProfileSkill.objects.create(profile=self.profile, description="list of skills")
        self.profile_hobby = ProfileHobby.objects.create(profile=self.profile, description="hobbies description")
        self.profile_language = ProfileLanguage.objects.create(profile=self.profile, description="list of languages")

        self.profile_data = {
            "user": self.user.pk,
            "profile": self.profile.pk,
            "language": self.language.pk,
            "gender": "male",
            "status": "Saved",
            "education": self.education.pk,
            "experience": self.experience.pk,
            "profile_skill": self.profile_skill.pk,
            "profile_hobby": self.profile_hobby.pk,
            "profile_language": self.profile_language.pk,
        }

        self.token = Token.objects.create(user=self.user)
        self.token_header = f"Token {self.token.key}"

    def test_profile_cannot_create_with_no_data(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.token_header)
        res = self.client.post(self.profile_route)
        self.assertEqual(res.status_code, 400)

    def test_profile_post(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.token_header)
        res = self.client.post(self.profile_route, self.profile_data, format="json")
        self.assertEqual(res.status_code, 201)
        