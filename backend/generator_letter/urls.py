from django.urls import path, include
from .views import update_application
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path("<int:pk>/", update_application),
]