from django.shortcuts import render
from django.conf import settings
from rest_framework import permissions, viewsets
from django.core.mail import EmailMessage
from rest_framework.response import Response

# Create your views here.
class Sendmail(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        email=request.data['to']
        emailw=EmailMessage(
            'test email Subject',
            'test email body, this msg is from python',
            settings.EMAIL_HOST_USER,
            [email]
        )
        
        # emailw.attach_file('manage.py')
        
        emailw.send(fail_silently=False)
        return Response({'status':True, 'message':'Email sent successfully'})