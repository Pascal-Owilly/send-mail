from django.shortcuts import render
import smtplib
from email.mime.text import MIMEText
from django.http import JsonResponse

# email views

def send_email(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')

    # composing email message

    msg = MIMEText(f"Name: {name}\nEmail: {email}\nMessage: {message}")
    msg['Subject'] = 'New message from your website'
    msg['From'] = 'mwani.africa@gmail.com'
    msg['To'] = 'mwani.africa@gmail.com'

    # send the email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('mwani.africa@gmail.com', 'Vzp.PK2$pGW2')
        server.sendmail('mwani.africa@gmail.com', ['mwani.africa@gmail.com'], msg.as_string())

    # Return a JSON response to client

    return JsonResponse({'success': True})




