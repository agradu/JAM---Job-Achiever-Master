from django.urls import path, include
from rest_framework import routers
from . import views
# from .views import SchedulerViewSet

router = routers.DefaultRouter()
# router.register("", SchedulerViewSet, basename="scheduler")

urlpatterns = [
    path("scheduler/", views.SchedulerViewSet.as_view(), name='scheduler'),
]
