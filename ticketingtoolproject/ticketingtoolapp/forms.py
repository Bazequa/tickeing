from django import forms
from django.contrib.auth.models import User
from .models import ProductsModel,ApplicationsModel,BookingsModel
from django.contrib.auth.forms import UserCreationForm

Choices=[(1,'Products'),(2,'Application'),(3,'Booking')]

class SelectType(forms.Form):
    select=forms.ChoiceField(choices=Choices,widget=forms.RadioSelect)

class ProductForm(forms.ModelForm):
    class Meta:
        model=ProductsModel
        fields='__all__'

class ApplicationForm(forms.ModelForm):
    class Meta:
        model=ApplicationsModel
        fields='__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model=BookingsModel
        fields='__all__'

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
