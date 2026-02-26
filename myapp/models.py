from django.db import models

# Create your models here.

class ContactModel(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class MassageBookingModel(models.Model):
    name=models.CharField(max_length=100)   
    phonenumber=models.CharField(max_length=20)
    email=models.EmailField(max_length=20,null=True,blank=True)
    massage_type=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)