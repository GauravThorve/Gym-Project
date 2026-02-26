from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from django.core.mail import send_mail
from django.conf import settings
import urllib


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

def contact(request):
    if request.method == "POST" :
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")

        ContactModel.objects.create(
            name=name,
            email=email,
            message=message,
        )
        send_mail(
            subject="New Contact Form has Came",
            message=f"Name : {name} \n Email : {email} \n Message : {message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["thorvegaurav4@gmail.com"],

        )
        print("Form Submitted")
        return redirect('contact')
    
    return render(request,'myapp/contact.html')

def location(request):
    return render(request,'myapp/location.html')

def personal_training(request):
    return render(request,'myapp/pt.html')

def try_us_view(request):
    return render(request,'myapp/try-us.html')

def inbody(request):
    return render(request,'myapp/inbody.html')