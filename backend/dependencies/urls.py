from django.urls import path, include
from rest_framework import routers
from .views import LanguageViewSet

router = routers.DefaultRouter()
router.register("language", LanguageViewSet, basename="languages")

urlpatterns = [
    path("", include(router.urls)),
]
