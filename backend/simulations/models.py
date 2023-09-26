from django.db import models
from users import models as users
from applications import models as applications
from dependencies import models as dependencies

# Create your models here.

class Simulation(models.Model):
    user_id = models.ForeignKey(users.User, on_delete=models.CASCADE)
    application_id = models.ForeignKey(applications.Application, on_delete=models.CASCADE)
    recruiter_attitude = models.CharField(max_length=150, null=True, blank=True)
    language_id = models.ForeignKey(dependencies.Language, on_delete=models.CASCADE)
    json_file = models.TextField(null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField()