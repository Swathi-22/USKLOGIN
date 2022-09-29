from django.contrib import admin
from .models import LatestNews, UserRegistration



@admin.register(UserRegistration)
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ( 'name','email','category',)


@admin.register(LatestNews)
class LatestNewsAdmin(admin.ModelAdmin):
    list_display =('news',)