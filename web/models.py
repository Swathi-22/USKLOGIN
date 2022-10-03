
from tabnanny import verbose
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

    def __str__(self):
        return str(self.news)



class NewServicePoster(models.Model):
    image = VersatileImageField('Image',upload_to='New_Service/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')

    class Meta:
        verbose_name_plural = ("New Service Poster")

    def __str__(self):
        return str(self.image)



class ImportantPoster(models.Model):
    image = VersatileImageField('Image',upload_to='Importants/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')

    class Meta:
        verbose_name_plural = ("Important Poster")

    def __str__(self):
        return str(self.image)



class CommonServicesPoster(models.Model):
    image = VersatileImageField('Image',upload_to='CommonServices/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')

    class Meta:
        verbose_name_plural = ("Common Services Poster")

    def __str__(self):
        return str(self.image)



class FestivelPoster(models.Model):
    image = VersatileImageField('Image',upload_to='FestivelPoster/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')

    class Meta:
        verbose_name_plural = ("Festivel Poster")

    def __str__(self):
        return str(self.image)



class ProfessionalPoster(models.Model):
    image = VersatileImageField('Image',upload_to='ProfessionalPoster/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')

    class Meta:
        verbose_name_plural = ("Professional Poster")

    def __str__(self):
        return str(self.image)



class GenerateForms(models.Model):
    file = models.FileField()
    name = models.CharField(max_length = 100)
    image = VersatileImageField('Image',upload_to='Forms/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')

    class Meta:
        verbose_name_plural = ("Generate Forms")

    def __str__(self):
        return str(self.name)
