from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.DateField(default=date(2000, 1, 1))
    gender = models.CharField(max_length=50, null=True, blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    social_link = models.URLField(max_length=255, null=True, blank=True)
    portfolio_link = models.URLField(max_length=255, null=True, blank=True)
    api_key = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.user.username})"


class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    school = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True)
    company = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.title


class ProfileSkill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.description


class ProfileHobby(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.description


class ProfileLanguage(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.description
