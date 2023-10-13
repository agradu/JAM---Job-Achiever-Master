from applications.models import Application
from rest_framework import serializers


class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["id"]
