from attr import fields
from django import forms
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput,ClearableFileInput, PasswordInput
from .models import *
from django.core.exceptions import ValidationError
import re


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = UserRegistration
#         fields = '__all__'
#         widgets= {
#             'name': TextInput(attrs={'class':'login__input','name':'name','id':'name','required':'required',}),
#             'password':TextInput(attrs={'class':'login__input','type':'password','name':'password','id':'password','required':'required',})
#         }



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


class SupportRequestForm(forms.ModelForm):
    # phone = forms.CharField(validators=[phone_number_validation])
    class Meta:
        model = SupportRequest
        fields = '__all__'
        widgets= {
            'name': TextInput(attrs={'class':'form-control','name':'name','id':'name','required':'required','autocomplete':'off',}),
            'phone': TextInput(attrs={'class':'form-control','name':'phoneno','id':'phoneno','required':'required','autocomplete':'off',}),
            'email': EmailInput(attrs={'class':'form-control','name':'email','id':'email','required':'required','autocomplete':'off',}),
            'message':Textarea(attrs={'class':"form-control",'name':"message",'id':'message','rows':"6",'autocomplete':'off',}),
            
        }



class SupportTicketForm(forms.ModelForm):
    # phone = forms.CharField(validators=[phone_number_validation])
    class Meta:
        model = SupportTicket
        fields = '__all__'
        widgets= {
            'name': TextInput(attrs={'class':'form-control','name':'name','id':'name','required':'required','autocomplete':'off',}),
            'phone': TextInput(attrs={'class':'form-control','name':'phoneno','id':'phoneno','required':'required','autocomplete':'off',}),
            'email': EmailInput(attrs={'class':'form-control','name':'email','id':'email','required':'required','autocomplete':'off',}),
            'message':Textarea(attrs={'class':"form-control",'name':"message",'id':'message','rows':"6",'autocomplete':'off',}),
            
        }



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = ['name','shop_name','shop_address','email','phone','profile_image','category']