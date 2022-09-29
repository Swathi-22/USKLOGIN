from django.urls import path
from . import views

app_name='services'

urlpatterns =[

    path('services-head/',views.serviceHead,name='serviceHead'),
    path('services/',views.service,name='service'),
    path('service-details/',views.serviceDetails,name='serviceDetails'),

]


