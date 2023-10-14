from django.urls import path, include
from rest_framework import routers
from .views import SimulationViewSet, SimulateInterviewWithGPT, AnalizeInterviewWithGPT

router = routers.DefaultRouter()
router.register("simulations", SimulationViewSet, basename="simulations")

urlpatterns = [
    path("", include(router.urls)),
    path("gpt/", SimulateInterviewWithGPT.as_view(), name="simulate-interview"),
    path("analize/", AnalizeInterviewWithGPT.as_view(), name="simulate-interview"),
]