from django.contrib import admin
from .models import Language, Gender, Status

# Register your models here.
admin.site.register(Language)
admin.site.register(Gender)
admin.site.register(Status)
