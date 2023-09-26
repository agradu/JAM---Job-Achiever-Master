from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.first_name
    
class Company(models.Model):
    company_name = models.CharField(max_length=30)

    def __str__(self):
        return self.company_name