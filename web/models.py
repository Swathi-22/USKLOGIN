from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class UserRegistration(models.Model):
    CATEGORY_CHOICES = (('AKSHAYA','AKSHAYA'),('CSC(DIGITAL INDIA)','CSC(DIGITAL INDIA'),('ONLINE SERVICE CENTER','ONLINE SERVICE CENTER'),('DTP AND PHOTOSTAT SHOP','DTP AND PHOTOSTAT SHOP'),('MOBILE SHOP','MOBILE SHOP'),('TRAVELS','TRAVELS'),('BANKING KIOSK','BANKING KIOSK'),('INTERNET CAFE','INTERNET CAFE'),('OTHERS','OTHERS'))
    name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    shop_address = models.TextField()
    email =  models.EmailField()
    phone = models.CharField(max_length=200)
    category = models.CharField(max_length=200,choices=CATEGORY_CHOICES) 