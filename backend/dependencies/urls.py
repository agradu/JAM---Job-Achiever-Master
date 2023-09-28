from django.urls import path, include
from rest_framework import routers
from .views import LanguageViewSet, GenderViewSet, StatusViewSet

router = routers.DefaultRouter()
router.register('item', LanguageViewSet, basename='languages')
router.register('item', GenderViewSet, basename='genders')
router.register('item', StatusViewSet, basename='statuses')

urlpatterns = [
    path('', include(router.urls)),
]
