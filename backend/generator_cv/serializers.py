from rest_framework import serializers
from applications.models import Application


class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["cv_short_description"]
