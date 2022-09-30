
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField
from .functions import generate_pk, generate_pw



class BaseModel(models.Model):
    id = models.CharField(default=generate_pk, primary_key=True, max_length=255, unique=True, blank=True)
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class UserRegistration(BaseModel):
    CATEGORY_CHOICES = (('AKSHAYA','AKSHAYA'),('CSC(DIGITAL INDIA)','CSC(DIGITAL INDIA)'),('ONLINE SERVICE CENTER','ONLINE SERVICE CENTER'),('DTP AND PHOTOSTAT SHOP','DTP AND PHOTOSTAT SHOP'),('MOBILE SHOP','MOBILE SHOP'),('TRAVELS','TRAVELS'),('BANKING KIOSK','BANKING KIOSK'),('INTERNET CAFE','INTERNET CAFE'),('OTHERS','OTHERS'))
    name = models.CharField(max_length=100)
    password = models.CharField(default=generate_pw, max_length=30, blank=True)
    shop_name = models.CharField(max_length=100)
    shop_address = models.TextField()
    email =  models.EmailField()
    phone = models.CharField(max_length=200)
    category = models.CharField(max_length=200,choices=CATEGORY_CHOICES)

    class Meta:
        verbose_name_plural = ("Users")

        def __str__(self):
            return str(self.name)


class LatestNews(models.Model):
    news = models.TextField()

    class Meta:
        verbose_name_plural = ("Lates News")



class NewServicePoster(models.Model):
    image = VersatileImageField('Image',upload_to='New_Service/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')

    class Meta:
        verbose_name_plural = ("New Service Poster")



class ImportantPoster(models.Model):
    image = VersatileImageField('Image',upload_to='Importants/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')

    class Meta:
        verbose_name_plural = ("Important Poster")
