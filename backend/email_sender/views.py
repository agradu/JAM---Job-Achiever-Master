from django.conf import settings
from rest_framework import permissions
from rest_framework.views import APIView
from django.core import mail
from rest_framework.response import Response
from applications.models import Application


class Sendmail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            application = Application.objects.get(pk=request.data["pk"])
            body = application.cover_letter_text
            body += f"\n\nhttp://18.157.164.150/api/v1/cv_generator/pdf/{request.data['pk']}/"

            # Create and send the email with the attached file
            email = mail.EmailMessage(
                subject=f"Application for: {application.position}",
                body=body,
                from_email=settings.EMAIL_HOST_USER,
                to=[application.company_email],
            )

            email.send(fail_silently=False)

            return Response({"status": True, "message": "Email sent successfully"})

        except Application.DoesNotExist:
            return Response(
                {"status": False, "message": "Application not found"}, status=404
            )
