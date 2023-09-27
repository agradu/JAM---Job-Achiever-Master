from django.db import models
from applications import models as applications
from users import models as users
# Create your models here.


class Scheduler(models.Model):
    user = models.ForeignKey(users.User, on_delete=models.CASCADE)
    application = models.ForeignKey(applications.Application, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} with {self.application.company} at {self.date}" 