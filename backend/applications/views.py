from rest_framework import viewsets
from rest_framework import permissions
from .models import Application
from .serializers import ApplicationsSerializer


class ApplicationsViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationsSerializer
    permission_classes = [permissions.IsAuthenticated]
