from django.shortcuts import render
from users.models import User, Education, Experience, UserSkill, UserLanguage, UserHobby
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
    #    user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=404)
    application.description = "Test done!"
    application.save()
    
    serializer = LetterSerializer(application)
    return Response(serializer.data)