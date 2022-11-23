from django.shortcuts import render,HttpResponseRedirect
<<<<<<< HEAD
from .forms import LoginForm, SelectType,ProductForm,ApplicationForm,BookingForm, SignUpForm
from .models import ProductModel,ApplicationModel,BookingModel
from django.contrib.auth import authenticate, login, logout
=======
from .forms import SelectType,ProductForm,ApplicationForm,BookingForm,SignUpForm
from .models import ProductModel,ApplicationModel,BookingModel

>>>>>>> 1f6d5f4364bed3e7548ac19bf8ed6826a19c2c69
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')
def employee(request):
    if request.method=='POST':
        fm=SelectType(request.POST)
        if fm.is_valid():
            if fm.fields['select'].choices[1]:
                return HttpResponseRedirect('/products')
            elif fm.fields['select'].choices[2]:
                return HttpResponseRedirect('/application')
            elif fm.fields['select'].choices[3]:
                return HttpResponseRedirect('/booking')
            else:
                return HttpResponseRedirect('/')
    else:
        fm=SelectType()
    return render(request,'employee.html',{'form':fm})
def manager(request):
    return render(request,'manager.html')
def admin(request):
    return render(request,'admin.html')
<<<<<<< HEAD

=======
>>>>>>> 1f6d5f4364bed3e7548ac19bf8ed6826a19c2c69
def products(request):
    if request.method=='POST':
        fm=ProductForm(request.POST)
    else:
        fm=ProductForm()
    return render(request,'products.html',{'form':fm})
def application(request):
    if request.method=='POST':
        fm=ApplicationForm(request.POST)
    else:
        fm=ApplicationForm()
    return render(request,'application.html',{'form':fm})
def booking(request):
    if request.method=='POST':
        fm=BookingForm(request.POST)
    else:
        fm=BookingForm()
    return render(request,'booking.html',{'form':fm})

<<<<<<< HEAD
=======

def login(request):
    return render(request,'login.html')


def signup(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully !!') 
            user = fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {'form':fm})


>>>>>>> 1f6d5f4364bed3e7548ac19bf8ed6826a19c2c69
