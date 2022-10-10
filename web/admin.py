from django.contrib import admin
from .models import *



@admin.register(UserRegistration)
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ( 'name','email','phone','category',)


@admin.register(LatestNews)
class LatestNewsAdmin(admin.ModelAdmin):
    list_display =('news',)


@admin.register(NewServicePoster)
class NewServicePosterAdmin(admin.ModelAdmin):
    list_display =('id','image',)


@admin.register(ImportantPoster)
class ImportantPosterAdmin(admin.ModelAdmin):
    list_display =('id','image',)


@admin.register(CommonServicesPoster)
class CommonServicesPosterAdmin(admin.ModelAdmin):
    list_display =('id','image',)


@admin.register(FestivelPoster)
class FestivelPosterAdmin(admin.ModelAdmin):
    list_display =('id','image',)


@admin.register(ProfessionalPoster)
class ProfessionalPosterAdmin(admin.ModelAdmin):
    list_display =('id','image',)


@admin.register(GenerateForms)
class GenerateFormsAdmin(admin.ModelAdmin):
    list_display =('name','file',)


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display =('name','file',)


@admin.register(Softwares)
class SoftwaresAdmin(admin.ModelAdmin):
    list_display =('name','link',)


@admin.register(Tools)
class ToolsAdmin(admin.ModelAdmin):
    list_display=('name','link',)


@admin.register(MarketingTips)
class MarketingTipsAdmin(admin.ModelAdmin):
    list_display=('name','link',)


@admin.register(OtherIdeas)
class OtherIdeasAdmin(admin.ModelAdmin):
    list_display=('name','link',)


@admin.register(AgencyPortal)
class AgencyPortalAdmin(admin.ModelAdmin):
    list_display=('name','link',)


@admin.register(BackOfficeServices)
class BackOfficeServicesAdmin(admin.ModelAdmin):
    list_display=('name','link',)


@admin.register(AgentBonus)
class AgentBonusAdmin(admin.ModelAdmin):
    list_display=('name','link',)


@admin.register(SupportRequest)
class SupportRequestAdmin(admin.ModelAdmin):
    list_display=('name','email','phone',)


@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display=('ticket_id','name','email','phone',)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display=('id','question',)