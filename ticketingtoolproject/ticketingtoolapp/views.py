from django.shortcuts import render,HttpResponseRedirect
from .forms import LoginForm, SelectType,ProductForm,ApplicationForm,BookingForm, SignUpForm
from .models import ProductModel,ApplicationModel,BookingModel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
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



# def user_login(request):
#   if not request.user.is_authenticated:
#     if request.method == "POST":
#       fm = AuthenticationForm(request=request, data=request.POST)
#       if fm.is_valid():
#         uname = fm.cleaned_data['username']
#         upass = fm.cleaned_data['password']
#         urole = fm.cleaned_data['roles']
#         user = authenticate(username=uname, password=upass,role=urole)
#         if user is not None:
#           login(request, user)
#           messages.success(request, 'Logged in successfully !!')
#           if urole=="Manager":
#                return HttpResponseRedirect('manager')
#           elif urole=="Employee":
#                return HttpResponseRedirect('employee')
#           elif urole=="Admin":
#                return HttpResponseRedirect('adminpage')
#         else:
#             fm = AuthenticationForm()
#         return render(request, 'login.html', {'form':fm})
#   else:
#     if user.role=="Manager":
#         return HttpResponseRedirect('manager')
#     elif user.role=="Employee":
#         return HttpResponseRedirect('employee')
#     elif user.role=="Admin":
#         return HttpResponseRedirect('adminpage')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Successfully')
                    return HttpResponseRedirect('/login')
        else:
            fm=AuthenticationForm()
            return render(request,"login.html",{'form':fm})
    else:
        return HttpResponseRedirect('/login')

def signup(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully !!') 
            user = fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {'form':fm})

def ulogout(request):
    logout(request)
    return HttpResponseRedirect('/')
