from django.urls import path
from . import views

app_name='services'

urlpatterns =[

    path('services-head/',views.serviceHead,name='serviceHead'),
    path('services/<slug:slug>/',views.service,name='service'),
    path('service-details/<slug:slug>/',views.serviceDetails,name='serviceDetails'),

]


