from django.db import models
from applications import models as applications
from profiles.models import Profile
# Create your models here.


class Scheduler(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    application = models.ForeignKey(applications.Application, on_delete=models.CASCADE)
    interview_shedule = models.DateTimeField()
    interview_time_before = models.TimeField()
    interview_time_after = models.TimeField()

    def __str__(self):
        return f"{self.user.username} with {self.application.company} at {self.date}" 