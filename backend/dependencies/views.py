from rest_framework import viewsets
from rest_framework import permissions
from .models import Language, Gender, Status
from .serialazers import LanguageSerialazer, GenderSerialazer, StatusSerialazer

# Create your views here.

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerialazer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GenderViewSet(viewsets.ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerialazer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerialazer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]