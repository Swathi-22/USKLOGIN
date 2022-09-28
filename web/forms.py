from django import forms
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput,ClearableFileInput, PasswordInput
from .models import *
from django.core.exceptions import ValidationError
import re




def phone_number_validation(value):
    if not re.compile(r'[0-9]\d{9}$').match(value):
        raise ValidationError('This is Not Valid Phone Number')


class UserRegistrationForm(forms.ModelForm):
    phone = forms.CharField(validators=[phone_number_validation])
    class Meta:
        model = UserRegistration
        fields = '__all__'
        widgets= {
            'name': TextInput(attrs={'class':'input-field','name':'name','id':'name','required':'required',}),
            'shop_name': TextInput(attrs={'class':'input-field','name':'shop_name','id':'shop_name','required':'required','autocomplete':'off',}),
            'shop_address': Textarea(attrs={'class':'input-field','name':'shop_address','id':'shop_address','required':'required','autocomplete':'off',}),
            'email': EmailInput(attrs={'class':'input-field','name':'email','id':'email','required':'required','autocomplete':'off',}),
            'category':Select(attrs={'class':'input-field','name':'category','id':'category','required':'required','autocomplete':'off',}),
            
        }


