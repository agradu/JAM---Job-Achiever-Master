from django.urls import path, include
from rest_framework import routers
from .views import SchedulerViewSet

router = routers.DefaultRouter()
router.register("schedulers", SchedulerViewSet, basename="scheduler")

urlpatterns = [
    path("", include(router.urls)),
]
