from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
import urllib
import os 
import resend
import logging

def home(request):
    return render(request,'myapp/home.html')

def about(request):
    return render(request,'myapp/about.html')

def service(request):
    if request.method == "POST":
        name=request.POST.get("name")  
        phonenumber=request.POST.get("phonenumber")
        email=request.POST.get("email")
        massage=request.POST.get("massage_type") 
        

        MassageBookingModel.objects.create(
            name=name,
            phonenumber=phonenumber,
            email=email,
            massage_type=massage,

        )
        message=f"New Massage Booking \n Name : {name} \n Email : {email} \n Phone Number : {phonenumber} \n Massage Type : {massage}"
        encoded_message=urllib.parse.quote(message)
        whatsapp_url=f"https://wa.me/919765221387?text={encoded_message}"

        return redirect(whatsapp_url)


    return render(request,'myapp/service.html')


resend.api_key = os.environ.get("RESEND_API_KEY")
# def contact(request):
#     if request.method == "POST" :
#         name=request.POST.get("name")
#         email=request.POST.get("email")
#         message=request.POST.get("message")
#         PhoneNumber = request.POST.get("phonenumber")
#
#         resend.Emails.send({
#             "from": "onboarding@resend.dev",
#             "to": "thorvegaurav4@gmail.com",
#             "subject": "New Contact Form Submission",
#             "html": f"""
#                 <h2>New Contact Form For BB Fitness Crew</h2>
#                 <p><strong>Name:</strong> {name}</p>
#                 <p><strong>Email:</strong> {email}</p>
#                 <p><strong>Message:</strong> {message}</p>
#             """
#         })
#
#         return redirect("/")
#
#     return render(request,'myapp/contact.html')

from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
import logging

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        enquiry = ContactModel.objects.create(
            name=name,
            email=email,
            phone=phone or "",
            message=message,
        )

        try:
            resend.Emails.send({
                "from": "onboarding@resend.dev",
                "to": ["thorvegaurav4@gmail.com"],
                "subject": f"New BB Fitness Crew Enquiry - {name}",
                "html": f"""
                    <h2>New BB Fitness Crew Enquiry</h2>
                    <p><strong>Name:</strong> {name}</p>
                    <p><strong>Email:</strong> {email}</p>
                    <p><strong>Phone:</strong> {phone}</p>
                    <p><strong>Message:</strong></p>
                    <p>{message}</p>
                """
            })

        except Exception:
            logging.getLogger(__name__).exception(
                "Could not send email notification for contact enquiry %s",
                enquiry.pk,
            )

        return render(
            request,
            "myapp/contact.html",
            {"success": "Thank you! Your message has been received."}
        )

    return render(request, "myapp/contact.html")









def location(request):
    return render(request,'myapp/location.html')

def personal_training(request):
    return render(request,'myapp/pt.html')

def try_us_view(request):
    return render(request,'myapp/try-us.html')

def inbody(request):
    return render(request,'myapp/inbody.html')
