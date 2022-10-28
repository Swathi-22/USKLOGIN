from .models import Customer
from .models import Invoice
from .models import InvoiceItem
from django.forms import ModelForm
from django.forms import inlineformset_factory


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ("name", "email", "phone_no", "address")


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = ("customer", "invoice_name", "invoice_no", "from_address", "phone_no")


class InvoiceItemForm(ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ("invoice", "services_name", "services_charge", "username", "password", "descripton", "qty")


InvoiceItemFormset = inlineformset_factory(Invoice, InvoiceItem, extra=1, can_delete=False)
InvoiceFormset = inlineformset_factory(Customer, Invoice, form=InvoiceForm, extra=1, can_delete=False)
