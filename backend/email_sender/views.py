from django.shortcuts import render
from django.conf import settings
from rest_framework import permissions
from rest_framework.views import APIView
from django.core.mail import EmailMessage
from rest_framework.response import Response
import smtplib

# Create your views here.
class Sendmail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        sender = settings.EMAIL_HOST_USER,
        receivers = [settings.EMAIL_HOST_USER]
        body='test email body, this msg is from python'
        try:
            smtp_object = smtplib.SMTP("localhost")
            smtp_object.sendmail(sender, receivers, body)
            print("Email succesfully sent.")
        except:
            print("Something happened...")
            
        
        
        # # breakpoint()
        # email=[request.data['to']]
        # emailw=EmailMessage(
        #     subject='test email Subject',
        #     body='test email body, this msg is from python',
        #     from_email=settings.EMAIL_HOST_USER,
        #     to=[settings.EMAIL_HOST_USER],
        # )
        
        # # emailw.attach_file('manage.py')
        
        # emailw.send(fail_silently=False)
        # return Response({'status':True, 'message':'Email sent successfully'})
        