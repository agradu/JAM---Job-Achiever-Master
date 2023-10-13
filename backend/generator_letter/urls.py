from django.urls import path, include
from .views import UpdateCoverLetter, DownloadCoverLetter


urlpatterns = [
    path("<int:pk>/", UpdateCoverLetter.as_view(), name="Update Cover Letter"),
    path("pdf/<int:pk>/", DownloadCoverLetter.as_view(), name="Download Cover Letter"),
]
