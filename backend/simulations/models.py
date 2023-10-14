from django.db import models
from django.contrib.auth.models import User
from applications.models import Application
from dependencies.models import Language

# Create your models here.


class Simulation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    recruiter_attitude = models.CharField(max_length=150, null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=8)
    json_file = models.JSONField(default=list)
    review = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.application.position} -> {self.application.company} ({self.created_at})"
