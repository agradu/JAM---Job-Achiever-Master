from django.db import models

# Create your models here.


class Language(models.Model):
    language = models.CharField(max_length=100, default="English", unique=True)

    def __str__(self):
        return self.language
