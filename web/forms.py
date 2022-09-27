from django import forms
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput,ClearableFileInput, PasswordInput
from .models import *


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = '__all__'
        widgets= {
            'name': TextInput(attrs={'class':'input-field','name':'name','id':'name','required':'required','autocomplete':'off',}),
            'shop_name': TextInput(attrs={'class':'input-field','name':'shop_name','id':'shop_name','required':'required','autocomplete':'off',}),
            'shop_address': Textarea(attrs={'class':'input-field','name':'shop_address','id':'shop_address','required':'required','autocomplete':'off',}),
            'email': EmailInput(attrs={'class':'input-field','name':'email','id':'email','required':'required','autocomplete':'off',}),
            'phone': TextInput(attrs={'class':'input-field','name':'mob_number','id':'mob_number','required':'required','autocomplete':'off',}),
            'category':Select(attrs={'class':'input-field','name':'category','id':'category','required':'required','autocomplete':'off',}),
            
        }


