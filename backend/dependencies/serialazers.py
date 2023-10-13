from .models import Language, Gender, Status
from rest_framework import serializers


class LanguageSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class GenderSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = "__all__"


class StatusSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"
