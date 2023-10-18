from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from .views import SchedulerViewSet

router = routers.DefaultRouter()
router.register("", SchedulerViewSet, basename="scheduler")

urlpatterns = [
    path("", SchedulerViewSet.as_view(), name='scheduler'),
    # path("", include(router.urls)),
]
