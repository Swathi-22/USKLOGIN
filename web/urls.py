import django
from django.urls import path
from . import views
from django.views.static import serve

app_name='web'

urlpatterns =[

    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('forgot-password/',views.forgot_password,name='forgot_password'),
    path('profile/',views.profile,name='profile'),
    path('settings/',views.settings,name='settings'),
    path('dashboard/',views.index,name='index'),
    path('generate-poster/',views.generatePoster,name='generatePoster'),
    path('generate-bill/',views.generateBill,name='generateBill'),
    path('invoice/',views.invoice,name='invoice'),
    path('generate-form/',views.generateForms,name='generateForms'),
    path('download/', serve, {'document_root': 'settings.MEDIA_ROOT'}),
    path('documents/',views.documents,name='documents'),
    path('softwares/',views.software,name='software'),
    path('tools/',views.tools,name='tools'),
    path('marketing-tip/',views.marketingTip,name='marketingTip'),
    path('other-ideas/',views.otherIdea,name='otherIdea'),
    path('agency-portal/',views.agencyPortal,name='agencyPortal'),
    path('back-office-services/',views.backOfficeServices,name='backOfficeServices'),
    path('bonus/',views.bonus,name='bonus'),
    path('support/',views.support,name='support'),
    path('terms-and-conditions/',views.termsConditions,name='termsConditions'),
    path('payment/',views.order_payment,name='order_payment'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('paymentsuccess/',views.paymentsuccess,name='paymentsuccess'),
    path('paymentfail/',views.paymentfail,name="paymentfail"),



]