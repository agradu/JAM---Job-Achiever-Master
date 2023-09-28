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
router.register("item", UserViewSet, basename="users")
router.register("item", EducationViewSet, basename="education")
router.register("item", ExperienceViewSet, basename="experience")
router.register("item", UserSkillViewSet, basename="userskills")
router.register("item", UserLanguageViewSet, basename="userlanguage")
router.register("item", UserHobbyViewSet, basename="userhobby")

urlpatterns = [
    path("", include(router.urls)),
]
