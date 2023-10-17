from rest_framework.test import APITestCase
from django.urls import reverse
from dependencies.models import Language, Gender, Status


class TestViews(APITestCase):
    def SetUp(self):
        pass

    def test_user_chooses_English(self):
        pass
