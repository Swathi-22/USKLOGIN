from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField
from tinymce.models import HTMLField
# Create your models here.


class ServiceHeads(models.Model):
    title = models.CharField(max_length = 225)
    slug=models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = ("Service Head")
    
    def __str__(self):
        return str(self.title)

    def get_services(self):
        return Services.objects.filter(service_head=self)


class Services(models.Model):
    service_head = models.ForeignKey(ServiceHeads,on_delete=models.CASCADE)   
    title = models.CharField(max_length = 225)
    image = VersatileImageField('Image',upload_to='service/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')
    link_to_official_website = models.URLField()
    about_service = HTMLField(blank=True, null=True)
    requirements = HTMLField(blank= True,null=True)
    service_charge = models.IntegerField()
    actual_service_charge = models.IntegerField()
    time_for_service = models.CharField(max_length=100)
    video_tutorial = models.CharField(max_length=100)
    guidline = models.CharField(max_length=100)
    upload_form = models.FileField()
    slug=models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = ("Services")

    def __str__(self):
        return str(self.title)    