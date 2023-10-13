from rest_framework import serializers
from .models import Application


class ApplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"
