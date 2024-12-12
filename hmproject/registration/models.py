from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#model for hotel details
class Hotel_Registration(models.Model):
    hotel_id = models.CharField(blank=False,max_length=100) #check need or not
    hotel_name = models.CharField(blank=False,max_length=100)
    hotel_place = models.CharField(blank=True,max_length=100)
    hotel_phone = models.CharField(blank=True,max_length=100)
    hotel_adress = models.CharField(blank=True,max_length=500)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.hotel_name

# users access to the system    
class User_Info(models.Model):
    Roll_Choices = [
        ('admin','Admin'),
        ('sub_admin','Sub_Admin'),
        ('customer','Customer')
    ]
   
    role = models.CharField(max_length=20, choices=Roll_Choices, default='customer')  
    phonenumber = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    
#customer details
class Customer(models.Model):   
    Status_Choice = [
        ('check_in','Check_in'),  #cuurently using the room facility
        ('waiting','Waiting'), #waiting for room facility
        ('check_out','Check_out')  #finished 
        
    ]
    customer_id = models.CharField(max_length=15, null=True, blank=True) #autogenerate
    customer_name = models.CharField(max_length=20, null=True, blank=True)   
    customer_phone = models.CharField(max_length=15, null=True, blank=True)
    customer_adress = models.CharField(blank=True,max_length=500)
    customer_email = models.CharField(max_length=20, null=True, blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer_profile') 
    customer_points = models.IntegerField(default=0) 
    customer_is_premium = models.BooleanField(default=False)
    customer_status=models.CharField(max_length=20, choices=Status_Choice, default='waiting')
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.Customer_name
    

#room details
class Room(models.Model):
    Room_Choices = [
        ('single','Single'),
        ('double','Double'),
        ('deluxe','Deluxe')
    ]
    room_number = models.CharField(max_length=10, unique=True)  # Unique room number
    room_type = models.CharField(max_length=20, choices=Room_Choices)
    room_description = models.TextField(blank=True, null=True)
    room_price = models.DecimalField(max_digits=10, decimal_places=2)
    room_is_available = models.BooleanField(default=True)  # Room availability status
    def __str__(self):
        return self.room_number