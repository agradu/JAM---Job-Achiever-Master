from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Profile,
    Education,
    Experience,
    ProfileSkill,
    ProfileLanguage,
    ProfileHobby,
)

# Register your models here.
admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(ProfileSkill)
admin.site.register(ProfileLanguage)
admin.site.register(ProfileHobby)
