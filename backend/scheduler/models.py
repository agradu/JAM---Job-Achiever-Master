from django.db import models

# Create your models here.

<<<<<<< HEAD
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
=======

class Sheduler(models.Model):
    user = models.ForeignKey(users.User, on_delete=models.CASCADE)
    application = models.ForeignKey(applications.Application, on_delete=models.CASCADE)
    date = models.DateTimeField()
>>>>>>> 12b52f0 (Fix the bug in serializers and views)

    def __str__(self):
        return self.first_name
    
class Company(models.Model):
    company_name = models.CharField(max_length=30)

    def __str__(self):
        return self.company_name