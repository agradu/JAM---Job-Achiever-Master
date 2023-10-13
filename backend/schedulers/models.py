from django.db import models
from django.contrib.auth.models import User
from applications.models import Application

# Create your models here.


class Scheduler(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    interview_shedule = models.DateTimeField()
    interview_time_before = models.TimeField()
    interview_time_after = models.TimeField()

    def __str__(self):
        return f"{self.user.username} with {self.application.company} at {self.interview_shedule}"
