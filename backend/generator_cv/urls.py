from django.urls import path, include
from .views import UpdateCvDescription, generate_pdf


urlpatterns = [
    path("<int:pk>/", UpdateCvDescription.as_view(), name="Update CV description"),
    path("pdf/<int:pk>/", generate_pdf, name="Generate PDF"),
]
