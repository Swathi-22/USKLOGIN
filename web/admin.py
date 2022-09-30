from django.contrib import admin
from .models import LatestNews, UserRegistration,NewServicePoster,ImportantPoster



@admin.register(UserRegistration)
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ( 'name','email','category',)


@admin.register(LatestNews)
class LatestNewsAdmin(admin.ModelAdmin):
    list_display =('news',)


@admin.register(NewServicePoster)
class NewServicePosterAdmin(admin.ModelAdmin):
    list_display =('id','image',)


@admin.register(ImportantPoster)
class ImportantPosterAdmin(admin.ModelAdmin):
    list_display =('id','image',)