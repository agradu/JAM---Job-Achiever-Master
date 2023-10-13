from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile
from dependencies import models as dependencies

# Create your models here.


class Application(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    cover_letter_text = models.TextField(blank=True)
    cv_short_description = models.CharField(max_length=400, blank=True)
    company_email = models.EmailField(max_length=255)
    company_address = models.CharField(max_length=255, blank=True)
    source = models.CharField(max_length=255, blank=True)
    recruiter_name = models.CharField(max_length=255, default="John Doe")
    recruiter_gender = models.ForeignKey(
        dependencies.Gender, on_delete=models.SET_DEFAULT, default=1
    )
    recruiter_position = models.CharField(max_length=255, default="CEO")
    application_language = models.ForeignKey(
        dependencies.Language, on_delete=models.SET_DEFAULT, default=1
    )
    status = models.ForeignKey(
        dependencies.Status, on_delete=models.SET_DEFAULT, default=1
    )
    status_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.position} - {self.company} ({self.created_at})"
