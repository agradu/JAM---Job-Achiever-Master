from django.db import models
from dependencies import models as dependencies


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    birthday = models.DateField(null=True)
    gender = models.ForeignKey(dependencies.Gender, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, null=True)
    phone = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True)
    social_link = models.CharField(max_length=50, null=True)
    portfolio_link = models.CharField(max_length=50, null=True)
    api_key = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    school = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True)
    company = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.title


class UserSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.description


class UserHobby(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.description


class UserLanguage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.description
