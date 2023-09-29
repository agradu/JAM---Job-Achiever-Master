from django.shortcuts import render
from profiles.models import Profile, Education, Experience, ProfileSkill, ProfileLanguage, ProfileHobby
from applications.models import Application
from rest_framework import viewsets
from rest_framework.decorators import api_view
import json
from datetime import date
import openai
from .serializers import LetterSerializer
from rest_framework.response import Response



@api_view(['GET'])
def update_application(request, pk):
    try:
        application = Application.objects.get(pk=pk) 
    #    user = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return Response(status=404)
    application.description = "Test done!"
    application.save()
    
    serializer = LetterSerializer(application)
    return Response(serializer.data)