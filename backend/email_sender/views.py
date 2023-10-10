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
        # breakpoint()
        with mail.get_connection() as connection:
            mail.EmailMessage(
                subject='test email Subject',
                body='Test email body, this msg comes from Django',
                from_email=settings.EMAIL_HOST_USER,
                to=[settings.EMAIL_HOST_USER],
        ).send()
        
        # emailw.attach_file('manage.py')
        
        return Response({'status':True, 'message':'Email sent successfully'})