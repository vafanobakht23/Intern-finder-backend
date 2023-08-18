from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
import certifi
from django.http import HttpResponse  
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["POST"])
def send_email(request):
    subject = 'Thank you for registering to our site'
    message = 'message'
    email_from = settings.EMAIL_HOST_USER
    recived_data = request.data
    recipient_list = [recived_data]
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse('Sent')

# email in person