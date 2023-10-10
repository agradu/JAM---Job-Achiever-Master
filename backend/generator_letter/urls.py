from django.urls import path, include
from .views import UpdateCoverLetter


urlpatterns = [
    path("<int:pk>/", UpdateCoverLetter.as_view(), name="Update Cover Letter"),
]