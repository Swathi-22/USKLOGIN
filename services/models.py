from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField
# Create your models here.


class ServiceHeads(models.Model):
    title = models.CharField(max_length = 225)
    slug=models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = ("Service Head")


class Services(models.Model):
    service_head = models.ForeignKey(ServiceHeads,on_delete=models.CASCADE)   
    title = models.CharField(max_length = 225)
    image = VersatileImageField('Image',upload_to='service/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')
    slug=models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = ("Services")
    