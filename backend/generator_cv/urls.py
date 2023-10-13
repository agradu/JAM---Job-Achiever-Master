from django.urls import path, include
from .views import UpdateCvDescriptionWithGPT, GeneratePdf


urlpatterns = [
    path("<int:pk>/", UpdateCvDescriptionWithGPT.as_view(), name="update-cv-description"),
    path("pdf/<int:pk>/", GeneratePdf.as_view(), name="generate-pdf"),
]
