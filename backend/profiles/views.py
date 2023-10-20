from rest_framework import viewsets, permissions
from .serializers import (
    ProfileSerializer,
    EducationSerializer,
    ExperienceSerializer,
    ProfileSkillSerializer,
    ProfileLanguageSerializer,
    ProfileHobbySerializer,
)
from .models import (
    Profile,
    Education,
    Experience,
    ProfileSkill,
    ProfileLanguage,
    ProfileHobby,
)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(profile__user=self.request.user)


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(profile__user=self.request.user)


class ProfileSkillViewSet(viewsets.ModelViewSet):
    queryset = ProfileSkill.objects.all()
    serializer_class = ProfileSkillSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(profile__user=self.request.user)


class ProfileLanguageViewSet(viewsets.ModelViewSet):
    queryset = ProfileLanguage.objects.all()
    serializer_class = ProfileLanguageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(profile__user=self.request.user)


class ProfileHobbyViewSet(viewsets.ModelViewSet):
    queryset = ProfileHobby.objects.all()
    serializer_class = ProfileHobbySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(profile__user=self.request.user)
