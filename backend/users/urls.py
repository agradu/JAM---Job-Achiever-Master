from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, EducationViewSet, ExperienceViewSet, UserSkillViewSet, UserLanguageViewSet, UserHobbyViewSet

router = DefaultRouter()
router.register('user', UserViewSet, basename='user')
router.register('education', EducationViewSet, basename='education')
router.register('experience', ExperienceViewSet, basename='experience')
router.register('userskills', UserSkillViewSet, basename='userskills')
router.register('userlanguage', UserLanguageViewSet, basename='userlanguage')
router.register('userhobby', UserHobbyViewSet, basename='userhobby')

urlpatterns = [
    path('', include(router.urls)),
]
