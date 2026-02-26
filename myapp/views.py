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


resend.api_key = os.environ.get("RESEND_API_KEY")
def contact(request):
    if request.method == "POST" :
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")

      
        resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": "thorvegaurav4@gmail.com",
            "subject": "New Contact Form Submission",
            "html": f"""
                <h2>New Contact Form For BB Fitness Crew</h2>
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Message:</strong> {message}</p>
            """
        })

        return redirect("/")
    
    return render(request,'myapp/contact.html')

def location(request):
    return render(request,'myapp/location.html')

def personal_training(request):
    return render(request,'myapp/pt.html')

def try_us_view(request):
    return render(request,'myapp/try-us.html')

def inbody(request):
    return render(request,'myapp/inbody.html')
