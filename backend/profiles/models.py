from django.db import models
from dependencies import models as dependencies
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Profile(AbstractUser):
    picture = models.ImageField(upload_to="profile_pictures/", null=True, blank=True)
    birthday = models.DateField(default=timezone.now)
    gender = models.ForeignKey(dependencies.Gender, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    social_link = models.URLField(max_length=255, null=True, blank=True)
    portfolio_link = models.URLField(max_length=255, null=True, blank=True)
    api_key = models.CharField(max_length=100, null=True, blank=True)

    # Specify custom related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Custom related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Custom related_name
        blank=True,
        help_text='Specific permissions for this user.',
    )
    
    def __str__(self):
        return self.username





class Education(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    school = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True)
    company = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.title


class ProfileSkill(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.description


class ProfileHobby(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.description


class ProfileLanguage(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.description
