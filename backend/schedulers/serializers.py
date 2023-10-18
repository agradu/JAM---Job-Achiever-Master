from .models import Scheduler
from rest_framework import serializers


class SchedulerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheduler
        fields = "__all__"
