from django.db import models

# Create your models here.

class ContactModel(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=20, blank=True, default="")
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


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=150)
    experience = models.PositiveIntegerField(default=0)
    photo = models.ImageField(upload_to="trainers/")
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
