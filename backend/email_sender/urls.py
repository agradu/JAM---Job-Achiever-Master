from django.contrib import admin
from django.urls import path, include
from .views import Sendmail

urlpatterns = [path("mail/", Sendmail.as_view(), name="sendmail")]
