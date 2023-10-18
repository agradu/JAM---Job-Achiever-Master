from rest_framework.views import APIView
from rest_framework import permissions
from .serialazers import SchedulerSerialazer
from .models import Scheduler

# Create your views here.


class SchedulerViewSet(APIView):
    queryset = Scheduler.objects.all()
    serializer_class = SchedulerSerialazer
    permission_classes = [permissions.IsAuthenticated]
