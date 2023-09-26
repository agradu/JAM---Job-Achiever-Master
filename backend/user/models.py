from django.db import models
from dependencies import models as dependencies 


class Users(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    birthday = models.DateTimeField()
    gender_id = models.ForeignKey(dependencies.Genders, on_delete=models.CASCADE) 
    email = models.EmailField(max_length = 254)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    social_link = models.CharField(max_length=50)
    portfolio_link = models.CharField(max_length=50)
    api_key = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user
    
class Educations(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    
class Experiences(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    
class UserSkills(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    description = models.CharField(50)
    
class UserHobbies(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    description = models.CharField(50)
    
class UserLanguages(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    description = models.CharField(50)