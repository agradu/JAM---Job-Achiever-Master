from django.urls import path, include
from rest_framework import routers
from .views import LanguageViewSet, GenderViewSet, StatusViewSet

router = routers.DefaultRouter()
router.register('language', LanguageViewSet, basename='languages')
router.register('gender', GenderViewSet, basename='genders')
router.register('status', StatusViewSet, basename='statuses')

urlpatterns = [
    path('', include(router.urls)),
]
