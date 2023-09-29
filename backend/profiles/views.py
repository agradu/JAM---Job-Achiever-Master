from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
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

class ProfileDetailView(generics.RetrieveDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class ProfileSkillViewSet(viewsets.ModelViewSet):
    queryset = ProfileSkill.objects.all()
    serializer_class = ProfileSkillSerializer


class ProfileLanguageViewSet(viewsets.ModelViewSet):
    queryset = ProfileLanguage.objects.all()
    serializer_class = ProfileLanguageSerializer


class ProfileHobbyViewSet(viewsets.ModelViewSet):
    queryset = ProfileHobby.objects.all()
    serializer_class = ProfileHobbySerializer