from django.db import models

# Create your models here.

class Languages(models.Model):
  language = models.CharField(max_length=100)

class Genders(models.Model):
  gender = models.CharField(max_length=50)

class Statuses(models.Model):
  status = models.CharField(max_length=100)