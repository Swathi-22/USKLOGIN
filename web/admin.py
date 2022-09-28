from django.contrib import admin
from .models import UserRegistration,Order



@admin.register(UserRegistration)
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ( 'name','email','category',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ( 'name',)

