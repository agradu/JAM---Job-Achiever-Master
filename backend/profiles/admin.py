from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, Education, Experience, ProfileSkill, ProfileLanguage, ProfileHobby

# Register your models here.
class ProfileTemplate(UserAdmin):
    list_display = [
        "picture",
        "birthday",
        "gender",
        "phone",
        "address",
        "social_link",
        "portfolio_link",
        "api_key",        
    ]

admin.site.register(Profile, ProfileTemplate)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(ProfileSkill)
admin.site.register(ProfileLanguage)
admin.site.register(ProfileHobby)
