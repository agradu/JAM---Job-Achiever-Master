from django.conf import settings
from rest_framework import permissions
from rest_framework.views import APIView
from django.core import mail
from rest_framework.response import Response
from applications.models import Application


# Create your views here.
class Sendmail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            application = Application.objects.get(pk=request.data["pk"])
            email = mail.EmailMessage(
                subject=application.position,
                body=application.cover_letter_text,
                from_email=settings.EMAIL_HOST_USER,
                to=[application.company_email],
            )
            email.send(fail_silently=False)
            return Response({"status": True, "message": "Email sent successfully"})
        except:
            return Response(status=404)
