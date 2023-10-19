from rest_framework import viewsets
from rest_framework import permissions
from .models import Language
from .serializers import LanguageSerializer

# Create your views here.


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [permissions.IsAuthenticated]

