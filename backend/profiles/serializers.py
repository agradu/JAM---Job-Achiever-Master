from rest_framework import serializers
from .models import (
    Profile,
    Education,
    Experience,
    ProfileSkill,
    ProfileLanguage,
    ProfileHobby,
)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"


class ProfileSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileSkill
        fields = "__all__"


class ProfileLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileLanguage
        fields = "__all__"


class ProfileHobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileHobby
        fields = "__all__"
