from django.urls import path
from . import views

app_name='web'

urlpatterns =[

    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('forgot-password/',views.forgot_password,name='forgot_password'),
    path('profile/',views.profile,name='profile'),
    path('settings/',views.settings,name='settings'),
    path('dashboard/',views.index,name='index'),
    path('services-head/',views.serviceHead,name='serviceHead'),
    path('services/',views.service,name='service'),
    path('service-details/',views.serviceDetails,name='serviceDetails'),
    path('generate-poster/',views.generatePoster,name='generatePoster'),
    path('generate-bill/',views.generateBill,name='generateBill'),
    path('generate-form/',views.generateForms,name='generateForms'),
    path('documents/',views.documents,name='documents'),
    path('softwares/',views.software,name='software'),
    path('tools/',views.tools,name='tools'),
    path('marketing-tip/',views.marketingTip,name='marketingTip'),
    path('other-ideas/',views.otherIdea,name='otherIdea'),
    path('agency-portal/',views.agencyPortal,name='agencyPortal'),
    path('back-office-services/',views.backOfficeServices,name='backOfficeServices'),
    path('bonus/',views.bonus,name='bonus'),
    path('support/',views.support,name='support'),


]