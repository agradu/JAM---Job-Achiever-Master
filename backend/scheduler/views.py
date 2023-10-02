from rest_framework import viewsets
from rest_framework import permissions
from .serialazers import SchedulerSerialazer
from .models import Scheduler

# Create your views here.


class SchedulerViewSet(viewsets.ModelViewSet):
    queryset = Scheduler.objects.all()
    serializer_class = SchedulerSerialazer
    permission_classes = [permissions.IsAuthenticated]
