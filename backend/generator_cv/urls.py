from django.urls import path, include
from .views import UpdateCvDescription, DownloadCV


urlpatterns = [
    path("<int:pk>/", UpdateCvDescription.as_view(), name="Update CV description"),
    path("pdf/<int:pk>/", DownloadCV.as_view(), name="Download CV")
]
