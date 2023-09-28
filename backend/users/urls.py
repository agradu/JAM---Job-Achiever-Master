from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    EducationViewSet,
    ExperienceViewSet,
    UserSkillViewSet,
    UserLanguageViewSet,
    UserHobbyViewSet,
)

router = DefaultRouter()
router.register("user", UserViewSet, basename="users")
router.register("education", EducationViewSet, basename="education")
router.register("experience", ExperienceViewSet, basename="experience")
router.register("skill", UserSkillViewSet, basename="userskills")
router.register("language", UserLanguageViewSet, basename="userlanguage")
router.register("hobby", UserHobbyViewSet, basename="userhobby")

urlpatterns = [
    path("", include(router.urls)),
]
