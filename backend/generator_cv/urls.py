from django.urls import path, include
from .views import UpdateCvDescriptionWithGPT, DownloadCV


urlpatterns = [
    path(
        "<int:pk>/", UpdateCvDescriptionWithGPT.as_view(), name="Update CV description"
    ),
    path("pdf/<int:pk>/", DownloadCV.as_view(), name="Download CV"),
]
