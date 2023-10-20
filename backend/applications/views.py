from rest_framework import viewsets
from rest_framework import permissions
from .models import Application
from .serializers import ApplicationsSerializer


class ApplicationsViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return Application.objects.order_by("-created_at").all()
        else:
            return Application.objects.filter(profile__user=user).order_by(
                "-created_at"
            )
