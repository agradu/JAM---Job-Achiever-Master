from django.urls import path, include
from rest_framework import routers
from .views import ApplicationsViewSet

router = routers.DefaultRouter()
router.register("applications", ApplicationsViewSet, basename="applications")

urlpatterns = [
    path('', include(router.urls)),
    # Remove the line below, as it's conflicting with the router
    # path('applications/', ApplicationsViewSet.as_view(), name="applications")
]