from django.shortcuts import render
from .models import Users, Company
from rest_framework import viewsets
from rest_framework import permissions
from .serialazers import UsersSerialazer, CompanySerialazer

# Create your views here.
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all
    serializer_class = UsersSerialazer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all
    serializer_class = CompanySerialazer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]