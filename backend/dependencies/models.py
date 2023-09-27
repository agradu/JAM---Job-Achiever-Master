from django.db import models

# Create your models here.


class Language(models.Model):
    language = models.CharField(max_length=100)


class Gender(models.Model):
    gender = models.CharField(max_length=50)


class Status(models.Model):
    status = models.CharField(max_length=100)
