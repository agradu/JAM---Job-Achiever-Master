from django.contrib import admin
from .models import User, Education, Experience, UserSkill, UserLanguage, UserHobby

# Register your models here.
admin.site.register(User)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(UserSkill)
admin.site.register(UserLanguage)
admin.site.register(UserHobby)