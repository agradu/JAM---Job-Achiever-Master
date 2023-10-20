from django.db import models
from profiles.models import Profile
from dependencies.models import Language
from django.utils import timezone


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
    recruiter_gender = models.CharField(max_length=50, null=True, blank=True, choices=
[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    recruiter_position = models.CharField(max_length=255, default="CEO")
    application_language = models.ForeignKey(Language, on_delete=models.SET_DEFAULT, default=8)
    status = models.CharField(
        max_length=255,
        default="Saved",
        choices=[
            ("Saved", "Saved"),
            ("Applied", "Applied"),
            ("Scheduled", "Scheduled"),
            ("Accepted", "Accepted"),
            ("Rejected", "Rejected"),
        ],
    )
    status_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        self.status_date = timezone.now()
        return super(Application, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.position} - {self.company})"
