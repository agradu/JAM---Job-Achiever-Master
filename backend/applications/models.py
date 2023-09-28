from django.db import models
from django.utils import timezone
from users import models as users
from dependencies import models as dependencies

# Create your models here.


class Application(models.Model):
    user = models.ForeignKey(users.User, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    company_email = models.EmailField(max_length=255)
    company_adress = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    recruiter_name = models.CharField(max_length=255)
    recruiter_gender = models.ForeignKey(dependencies.Gender, on_delete=models.SET_DEFAULT, default=1)
    recruiter_position = models.CharField(max_length=255)
    application_language = models.ForeignKey(dependencies.Language, on_delete=models.SET_DEFAULT, default=1)
    status = models.ForeignKey(dependencies.Status, on_delete=models.SET_DEFAULT, default=1)
    status_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.position} - {self.company} ({self.created_at})"
