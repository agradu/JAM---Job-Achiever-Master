from django.shortcuts import render
from rest_framework import viewsets
from .serializers import (
    UserSerializer,
    EducationSerializer,
    ExperienceSerializer,
    UserSkillSerializer,
    UserLanguageSerializer,
    UserHobbySerializer,
)
from .models import User, Education, Experience, UserSkill, UserLanguage, UserHobby
from rest_framework import generics


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class EducationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class ExperienceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class UserSkillViewSet(viewsets.ModelViewSet):
    queryset = UserSkill.objects.all()
    serializer_class = UserSkillSerializer


class UserSkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserSkill.objects.all()
    serializer_class = UserSkillSerializer


class UserLanguageViewSet(viewsets.ModelViewSet):
    queryset = UserLanguage.objects.all()
    serializer_class = UserLanguageSerializer


class UserLanguageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserLanguage.objects.all()
    serializer_class = UserLanguageSerializer


class UserHobbyViewSet(viewsets.ModelViewSet):
    queryset = UserHobby.objects.all()
    serializer_class = UserHobbySerializer


class UserHobbyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserHobby.objects.all()
    serializer_class = UserHobbySerializer
