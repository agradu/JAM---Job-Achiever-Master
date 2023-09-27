from django.urls import path, include
from rest_framework import routers
from .views import ApplicationsViewSet

router = routers.DefaultRouter()
router.register("applications", ApplicationsViewSet, basename="applications")

urlpatterns = [
    path('', include(router.urls)),
]