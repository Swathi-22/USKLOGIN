from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
from .constants import PaymentStatus
from django.db.models.fields import CharField


class UserRegistration(models.Model):
    CATEGORY_CHOICES = (('AKSHAYA','AKSHAYA'),('CSC(DIGITAL INDIA)','CSC(DIGITAL INDIA)'),('ONLINE SERVICE CENTER','ONLINE SERVICE CENTER'),('DTP AND PHOTOSTAT SHOP','DTP AND PHOTOSTAT SHOP'),('MOBILE SHOP','MOBILE SHOP'),('TRAVELS','TRAVELS'),('BANKING KIOSK','BANKING KIOSK'),('INTERNET CAFE','INTERNET CAFE'),('OTHERS','OTHERS'))
    name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    shop_address = models.TextField()
    email =  models.EmailField()
    phone = models.CharField(max_length=200)
    category = models.CharField(max_length=200,choices=CATEGORY_CHOICES) 



class Order(models.Model):
    name = CharField(("Customer Name"), max_length=254, blank=False, null=False)
    amount = models.FloatField(("Amount"), null=False, blank=False)
    status = CharField(("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(("Signature ID"), max_length=128, null=False, blank=False
    )

    def __str__(self):
        return f"{self.id}-{self.name}-{self.status}"
