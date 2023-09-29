from rest_framework import serializers
from .models import Profile, Education, Experience, ProfileSkill, ProfileLanguage, ProfileHobby


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "username", "first_name", "last_name", "email", "picture", "birthday", "gender", "phone", "address", "social_link", "portfolio_link", "api_key"
        ]


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
