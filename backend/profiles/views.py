from rest_framework import viewsets
from rest_framework import permissions
from .serializers import (
    ProfileSerializer,
    EducationSerializer,
    ExperienceSerializer,
    ProfileSkillSerializer,
    ProfileLanguageSerializer,
    ProfileHobbySerializer,
)
from .models import Profile, Education, Experience, ProfileSkill, ProfileLanguage, ProfileHobby


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticated]


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfileSkillViewSet(viewsets.ModelViewSet):
    queryset = ProfileSkill.objects.all()
    serializer_class = ProfileSkillSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfileLanguageViewSet(viewsets.ModelViewSet):
    queryset = ProfileLanguage.objects.all()
    serializer_class = ProfileLanguageSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfileHobbyViewSet(viewsets.ModelViewSet):
    queryset = ProfileHobby.objects.all()
    serializer_class = ProfileHobbySerializer
    permission_classes = [permissions.IsAuthenticated]