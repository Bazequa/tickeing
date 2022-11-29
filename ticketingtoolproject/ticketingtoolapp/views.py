from django.shortcuts import render,HttpResponseRedirect
from .forms import  SelectType,ProductForm,ApplicationForm,BookingForm, SignUpForm
from .models import ProductModel,ApplicationModel,BookingModel
# from .models import Manager,Employee,AdminPage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')
def user_login(request):
  if not request.user.is_authenticated:
    if request.method == "POST":
      fm = AuthenticationForm(request=request, data=request.POST)
      if fm.is_valid():
        uname = fm.cleaned_data['username']
        upass = fm.cleaned_data['password']
        user = authenticate(username=uname, password=upass)
        admin_names=['bazequa','ramesh']
        if user is not None:
            if uname=='kalyan':
                login(request, user)
                messages.success(request, 'Logged in successfully !!')
                return HttpResponseRedirect('/manager')
            elif uname in admin_names:
                login(request, user)
                messages.success(request, 'Logged in successfully !!')
                return HttpResponseRedirect('/adminpage')
            else:
                login(request, user)
                messages.success(request, 'Logged in successfully !!')
                return HttpResponseRedirect('/emloyee')
    else:
        fm = AuthenticationForm()
    return render(request, 'login.html', {'form':fm})
  else:
        return HttpResponseRedirect('/')
    
def signup(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully !!')
            fm.save()
            return HttpResponseRedirect("/login/")
    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {'form':fm})

def ulogout(request):
    logout(request)
    return HttpResponseRedirect('/')


def products(request):
    if request.method=='POST':
        fm=ProductForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'data saved')
            fm.save()
            return HttpResponseRedirect('/employee')
    else:
        fm=ProductForm()
    return render(request,'products.html',{'form':fm})

def application(request):
    if request.method=='POST':
        fm=ApplicationForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'data saved')
            fm.save()
            return HttpResponseRedirect('/employee')
    else:
        fm=ApplicationForm()
    return render(request,'application.html',{'form':fm})

def booking(request):
    if request.method=='POST':
        fm=BookingForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'data saved')
            fm.save()
            return HttpResponseRedirect('/employee')
    else:
        fm=BookingForm()
    return render(request,'booking.html',{'form':fm})

def employee(request):
    return render(request,'employee.html')

def manager(request):
    # pfm=ProductModel.objects.all()
    # afm=ApplicationModel.objects.all()
    # bfm=BookingModel.objects.all()
    # # form={pfm:'pfm',afm:'afm','bfm':bfm}
    return render(request,'manager.html')

def admin(request):
    # pfm = ProductModel.objects.all()
    # afm = ApplicationModel.objects.all()
    # bfm = BookingModel.objects.all()
    return render(request,'admin.html')

