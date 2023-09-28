from django.urls import path, include
from rest_framework import routers
from .views import LanguageViewSet, GenderViewSet, StatusViewSet

router = routers.DefaultRouter()
router.register('languages', LanguageViewSet, basename='languages')
router.register('genders', GenderViewSet, basename='genders')
router.register('statuses', StatusViewSet, basename='statuses')

urlpatterns = [
    path('', include(router.urls)),
]
