from django.db import models
from django.utils import timezone
from users import models as users
from dependencies import models as dependencies
# Create your models here.

class Application(models.Model):
    user_id = models.ForeignKey(users.User, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    company_email = models.EmailField(max_length=255)
    company_adress = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    recruiter_name = models.CharField(max_length=255)
    recruiter_gender_id = models.ForeignKey(dependencies.Gender, on_delete=models.CASCADE)
    recruiter_position = models.CharField(max_length=255)
    application_language_id = models.ForeignKey(dependencies.Language, on_delete=models.CASCADE)
    status_id = models.ForeignKey(dependencies.Status, on_delete=models.CASCADE)
    status_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.position, self.company