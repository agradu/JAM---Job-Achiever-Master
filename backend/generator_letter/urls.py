from django.urls import path, include
from .views import UpdateCoverLetterWithGPT, DownloadCoverLetter


urlpatterns = [
    path("<int:pk>/", UpdateCoverLetterWithGPT.as_view(), name="Update Cover Letter"),
    path("pdf/<int:pk>/", DownloadCoverLetter.as_view(), name="Download Cover Letter"),
]
