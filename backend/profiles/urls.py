from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProfileViewSet,
    EducationViewSet,
    ExperienceViewSet,
    ProfileSkillViewSet,
    ProfileLanguageViewSet,
    ProfileHobbyViewSet,
)

router = DefaultRouter()
router.register("profile", ProfileViewSet, basename="profile")
router.register("education", EducationViewSet, basename="education")
router.register("experience", ExperienceViewSet, basename="experience")
router.register("skill", ProfileSkillViewSet, basename="profileskills")
router.register("language", ProfileLanguageViewSet, basename="profilelanguage")
router.register("hobby", ProfileHobbyViewSet, basename="profilehobby")

urlpatterns = [
    path("", include(router.urls)),
]
