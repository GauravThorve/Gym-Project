from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('service/', service, name='service'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('location/', location,name='location'),
    path('pt/', personal_training,name='pt'),
    path('tryus/', try_us_view,name='tryus'),
    path('inbody/', inbody,name='inbody')
    
]
