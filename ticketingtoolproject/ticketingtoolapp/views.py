from django.shortcuts import render,HttpResponseRedirect
from .forms import LoginForm, SelectType,ProductForm,ApplicationForm,BookingForm, SignUpForm
from .models import ProductModel,ApplicationModel,BookingModel
from django.contrib.auth import authenticate, login, logout
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

def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
    if form.is_valid():
        #messages.success(request, 'Congratulations!! You have become an Author.')
        user = form.save()
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form':form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !!')
                    return HttpResponseRedirect('/employee')
        else:
            form = LoginForm()
            return render(request, 'login.html', {'form':form})
    else:
        return HttpResponseRedirect('/employee')