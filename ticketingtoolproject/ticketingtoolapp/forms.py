from django import forms
from .models import ProductModel,ApplicationModel,BookingModel

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
Choices=[(1,'Products'),(2,'Application'),(3,'Booking')]
class SelectType(forms.Form):
    select=forms.ChoiceField(choices=Choices,widget=forms.RadioSelect)
class ProductForm(forms.ModelForm):
    class Meta:
        model=ProductModel
        fields='__all__'
class ApplicationForm(forms.ModelForm):
    class Meta:
        model=ApplicationModel
        fields='__all__'
class BookingForm(forms.ModelForm):
    class Meta:
        model=BookingModel
        fields='__all__'

roles = [('manager','manager'),('Employee','Employee'),('Admin','Admin')]

class SignUpForm(UserCreationForm):
 password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
 password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
 Role= forms.ChoiceField(required=False,widget=forms.CheckboxSelectMultiple,choices=roles)

 class Meta:
  model = User
  fields = ['username', 'first_name', 'last_name', 'email']
  labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}
  widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
  'first_name':forms.TextInput(attrs={'class':'form-control'}),
  'last_name':forms.TextInput(attrs={'class':'form-control'}),
  'email':forms.EmailInput(attrs={'class':'form-control'}),
#   'Role':forms.CheckboxSelectMultiple(Choices:roles)
  }