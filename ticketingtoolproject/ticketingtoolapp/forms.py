from django import forms
from .models import ProductModel,ApplicationModel,BookingModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = '__all__'
class LoginForm(AuthenticationForm):
    username = forms.CharField(label=("username"))
    password = forms.CharField(label=("Password"))