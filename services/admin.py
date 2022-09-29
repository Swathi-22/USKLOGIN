from django.contrib import admin
from . models import ServiceHeads,Services



@admin.register(ServiceHeads)
class ServiceHeadsAdmin(admin.ModelAdmin):
    list_display = ( 'title',)
    prepopulated_fields = {'slug':('title',)}


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ( 'service_head','title',)
    prepopulated_fields = {'slug':('title',)}