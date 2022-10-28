from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import InvoiceFormset, InvoiceItemFormset
from .models import Customer, Invoice


class CustomerList(ListView):
    model = Customer
    template_name = "invoice/customer_list.html"


class CustomerCreate(CreateView):
    model = Customer
    fields = ["name", "email", "phone_no"]
    template_name = "invoice/customer_form.html"


class CustomerInvoieCreate(CreateView):
    model = Customer
    fields = ["name", "email", "phone_no"]
    success_url = reverse_lazy("invoices:customer-list")
    template_name = "invoice/customer_form.html"

    def get_context_data(self, **kwargs):
        data = super(CustomerInvoieCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data["invoices"] = InvoiceFormset(self.request.POST)
        else:
            data["invoices"] = InvoiceFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        invoices = context["invoices"]
        with transaction.atomic():
            self.object = form.save()

            if invoices.is_valid():
                invoices.instance = self.object
                invoices.save()
        return super(CustomerInvoieCreate, self).form_valid(form)


class CustomerInvoieItemCreate(CreateView):
    model = Invoice
    fields = ["name", "email", "phone_no"]
    success_url = reverse_lazy("invoices:customer-list")
    template_name = "invoice/customer_form.html"

    def get_context_data(self, **kwargs):
        data = super(CustomerInvoieItemCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data["invoices_items"] = InvoiceItemFormset(self.request.POST)
        else:
            data["invoices_items"] = InvoiceItemFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        invoices = context["invoices_items"]
        with transaction.atomic():
            self.object = form.save()

            if invoices.is_valid():
                invoices.instance = self.object
                invoices.save()
        return super(CustomerInvoieCreate, self).form_valid(form)


class CustomerUpdate(UpdateView):
    model = Customer
    success_url = reverse_lazy("invoices:customer-list")
    fields = ["name", "email", "phone_no"]
    template_name = "invoice/customer_form.html"


class CustomerInvoieUpdate(UpdateView):
    model = Customer
    fields = ["name", "email", "phone_no"]
    success_url = reverse_lazy("invoices:customer-list")
    template_name = "invoice/customer_form.html"

    def get_context_data(self, **kwargs):
        data = super(CustomerInvoieUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data["invoices"] = InvoiceFormset(self.request.POST, instance=self.object)
        else:
            data["invoices"] = InvoiceFormset(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        invoices = context["invoices"]
        with transaction.atomic():
            self.object = form.save()

            if invoices.is_valid():
                invoices.instance = self.object
                invoices.save()
        return super(CustomerInvoieUpdate, self).form_valid(form)


class CustomerInvoieItemUpdate(UpdateView):
    model = Invoice
    fields = ["name", "email", "phone_no"]
    success_url = reverse_lazy("invoices:customer-list")
    template_name = "invoice/customer_form.html"

    def get_context_data(self, **kwargs):
        data = super(CustomerInvoieItemUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data["invoices"] = InvoiceItemFormset(self.request.POST)
        else:
            data["invoices"] = InvoiceItemFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        invoices = context["invoices"]
        with transaction.atomic():
            self.object = form.save()

            if invoices.is_valid():
                invoices.instance = self.object
                invoices.save()
        return super(CustomerInvoieCreate, self).form_valid(form)


class CustomerDelete(DeleteView):
    model = Customer
    success_url = reverse_lazy("invoices:customer-list")
    template_name = "invoice/customer_confirm_delete.html"
