from django.shortcuts import render,HttpResponseRedirect
from .forms import  SelectType,ProductForm,ApplicationForm,BookingForm, SignUpForm
from .models import ProductsModel,ApplicationsModel,BookingsModel
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
                return HttpResponseRedirect('/employee')
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
    pfm=ProductsModel.objects.all()
    afm=ApplicationsModel.objects.all()
    bfm=BookingsModel.objects.all()
    context={'pfm':pfm,'afm':afm,'bfm':bfm}
    return render(request,'manager.html', context )


def reject(request,id, model):
    if model=='1':
        pm=ProductsModel.objects.get(id=id)
        pm.delete()
        return HttpResponseRedirect('/manager')
    if model == '2':
        am = ApplicationsModel.objects.get(id=id)
        am.delete()
        return HttpResponseRedirect('/manager')
    if model == '3':
        bm = BookingsModel.objects.get(id=id)
        bm.delete()
        return HttpResponseRedirect('/manager')
    return HttpResponseRedirect('/manager')

def accept(request,id,model):
    if model == '2':
        am = ApplicationsModel.objects.get(id=id)
        request.session['one'] = 1
        request.session['one_id'] = id
    return HttpResponseRedirect('/manager')
    # if model=='1':
    #     pm=ProductModel.objects.get(id=id)
    #     request.session['pm'] = pm
    #     return HttpResponseRedirect('/manager')
    # if model == '2':
    #     print('---------')
    #     am = ApplicationModel.objects.get(id=id)
    #     request.session['am'] = am
    #     return HttpResponseRedirect('/manager')
    # if model == '3':
    #     bm = BookingModel.objects.get(id=id)
    #     request.session['bm'] = bm
    #     # return HttpResponseRedirect('/admin')
    # return HttpResponseRedirect('/manager')

def admin(request):
    pfm=ProductsModel.objects.all()
    afm=ApplicationsModel.objects.all()
    bfm=BookingsModel.objects.all()
    context={'pfm':pfm,'afm':afm,'bfm':bfm}
    return render(request,'admin.html', context )
    # am = request.session.get('one')
    # one_id = request.session.get('one_id')
    # if am == 1:
    #     am = ApplicationModel.objects.get(id=one_id)

    # context = {'am': am}
    # return render(request,'admin.html', context)