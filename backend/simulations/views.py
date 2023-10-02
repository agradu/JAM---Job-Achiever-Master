from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Simulation
from .serialazers import SimulationSerialazer

# Create your views here.
class SimulationViewSet(viewsets.ModelViewSet):
    queryset = Simulation.objects.all()
    serializer_class = SimulationSerialazer
    permission_classes = [permissions.IsAuthenticated]
