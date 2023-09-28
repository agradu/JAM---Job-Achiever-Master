from .models import Simulation
from rest_framework import serializers


class SimulationSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Simulation
        fields = "__all__"
