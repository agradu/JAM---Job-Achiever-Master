from django.shortcuts import render
from .models import User, Company
from rest_framework import viewsets
from rest_framework import permissions
from .serialazers import UsersSerialazer, CompanySerialazer

# Create your views here.
<<<<<<< HEAD
class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all
    serializer_class = UsersSerialazer
=======


class SchedulerViewSet(viewsets.ModelViewSet):
    queryset = Sheduler.objects.all
    serializer_class = ShedulerSerialazer
>>>>>>> 12b52f0 (Fix the bug in serializers and views)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all
    serializer_class = CompanySerialazer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]