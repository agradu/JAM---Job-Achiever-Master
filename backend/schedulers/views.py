from rest_framework import viewsets
from rest_framework import permissions
from .serializers import SchedulerSerializer
from .models import Scheduler

# Create your views here.


class SchedulerViewSet(viewsets.ModelViewSet):
    queryset = Scheduler.objects.all()
    serializer_class = SchedulerSerializer
    permission_classes = [permissions.IsAuthenticated]
