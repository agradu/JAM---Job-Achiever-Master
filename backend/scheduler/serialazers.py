from .models import Scheduler
from rest_framework import serializers


class SchedulerSerialazer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scheduler
        fields = ["user", "application", "date"]
