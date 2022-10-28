from django.urls import path

from . import views

app_name = "invoices"

urlpatterns = [
    path("", views.CustomerList.as_view(), name="customer-list"),
    path("/add/", views.CustomerInvoieCreate.as_view(), name="customer-add"),
    path("/update/<int:pk>", views.CustomerInvoieUpdate.as_view(), name="customer-update"),
    path("/delete/<int:pk>", views.CustomerDelete.as_view(), name="customer-delete"),
]
