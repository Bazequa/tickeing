from django import forms
from .models import ProductModel,ApplicationModel,BookingModel
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
