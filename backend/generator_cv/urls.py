from django.urls import path, include
from .views import UpdateCvDescription


urlpatterns = [
    path("<int:pk>/", UpdateCvDescription.as_view(), name="Update CV description"),
]