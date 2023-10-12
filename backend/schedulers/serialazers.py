from .models import Scheduler
from rest_framework import serializers


class SchedulerSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Scheduler
        fields = "__all__"
