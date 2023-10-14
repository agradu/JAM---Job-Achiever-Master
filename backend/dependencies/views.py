from rest_framework import viewsets
from rest_framework import permissions
from .models import Language, Gender, Status
from .serializers import LanguageSerializer, GenderSerializer, StatusSerialazer

# Create your views here.


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [permissions.IsAuthenticated]


class GenderViewSet(viewsets.ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
    permission_classes = [permissions.IsAuthenticated]


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerialazer
    permission_classes = [permissions.IsAuthenticated]
