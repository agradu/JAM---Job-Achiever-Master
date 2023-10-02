from django.urls import path, include
from rest_framework import routers
from .views import SimulationViewSet

router = routers.DefaultRouter()
router.register('item', SimulationViewSet, basename='simulations')

urlpatterns = [
    path('', include(router.urls)),
]