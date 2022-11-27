from django.shortcuts import render,HttpResponseRedirect
from .forms import  SelectType,ProductForm,ApplicationForm,BookingForm, SignUpForm,AuthenticationForm
from .models import ProductModel,ApplicationModel,BookingModel
# from .models import Manager,Employee,AdminPage
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.forms import AuthenticationForm
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
        urole = fm.cleaned_data['role']
        user = authenticate(username=uname, password=upass,role=urole)

        if user is not None and urole=='employee':
            login(request, user)
            messages.success(request, 'Logged in successfully !!')
            return HttpResponseRedirect('/employee')

        if user is not None and urole=='manager':
            login(request, user)
            messages.success(request, 'Logged in successfully !!')
            return HttpResponseRedirect('/manager')

        if user is not None and urole=='useradmin':
            login(request, user)
            messages.success(request, 'Logged in successfully !!')
            return HttpResponseRedirect('/adminpage')
        # if urole=="Manager":
        #        return render(request,'employee.html')
        #   elif urole=="Employee":
        #         return render(request,'manager.html')
        #   elif urole=="Admin":
        #         return render(request,'admin.html')
        #return render(request,'employee.html')
    else:
        fm = AuthenticationForm()
    return render(request, 'login.html', {'form':fm})
  else:
        return HttpResponseRedirect('/employee')
    # if user.role=="Manager":
    #     return HttpResponseRedirect('manager')
    # elif user.role=="Employee":
    #     return HttpResponseRedirect('employee')
    # elif user.role=="Admin":
    #     return HttpResponseRedirect('adminpage')




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


def employee(request):
    return render(request,'employee.html')
def manager(request):
    pfm=ProductModel.objects.all()
    afm=ApplicationModel.objects.all()
    bfm=BookingModel.objects.all()
    # form={pfm:'pfm',afm:'afm','bfm':bfm}
    return render(request,'manager.html',{pfm:'pfm',afm:'afm','bfm':bfm})
def admin(request):
    pfm = ProductModel.objects.all()
    afm = ApplicationModel.objects.all()
    bfm = BookingModel.objects.all()
    return render(request,'admin.html',{pfm:'pfm',afm:'afm','bfm':bfm})

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



