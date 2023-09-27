from django.shortcuts import render
from .models import Scheduler
from rest_framework import viewsets
from rest_framework import permissions
from .serialazers import SchedulerSerialazer

# Create your views here.


class SchedulerViewSet(viewsets.ModelViewSet):
    queryset = Scheduler.objects.all()
    serializer_class = SchedulerSerialazer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
