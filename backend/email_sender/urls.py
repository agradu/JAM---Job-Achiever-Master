from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Sendmail

urlpatterns = [path("mail/", Sendmail.as_view(), name="sendmail")]
