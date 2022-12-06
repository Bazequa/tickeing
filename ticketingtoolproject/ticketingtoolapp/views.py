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
            model = ProductsModel(user=request.user, Products=request.POST.get('Products'), Reason=request.POST.get('Reason'))
            model.save()
            
            return HttpResponseRedirect('/employee')
    else:
        fm=ProductForm()
    return render(request,'products.html',{'form':fm})

def application(request):
    if request.method=='POST':
        fm=ApplicationForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'data saved')
            model = ApplicationsModel(user=request.user, application=request.POST.get('application'), Reason=request.POST.get('Reason'))
            model.save()
           
            return HttpResponseRedirect('/employee')
    else:
        fm=ApplicationForm()
    return render(request,'application.html',{'form':fm})

def booking(request):

    if request.method=='POST':
        fm=BookingForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'data saved')
            model = BookingsModel(user=request.user, booking=request.POST.get('booking'), Reason=request.POST.get('Reason'))
            model.save()
            return HttpResponseRedirect('/employee')
    else:
        fm=BookingForm()
    return render(request,'booking.html',{'form':fm})

def employee(request):
    pfm=ProductsModel.objects.all()
    afm=ApplicationsModel.objects.all()
    bfm=BookingsModel.objects.all()
    context={'pfm':pfm,'afm':afm,'bfm':bfm}
    return render(request,'employee.html',context)

def manager(request):
    pfm=ProductsModel.objects.all()
    afm=ApplicationsModel.objects.all()
    bfm=BookingsModel.objects.all()
    context={'pfm':pfm,'afm':afm,'bfm':bfm}
    return render(request,'manager.html', context )


def reject(request,id, model):
    if model==1:
        rpm=ProductsModel.objects.get(id=id)
        rpm.reject_status=1
        rpm.save()
        # reject=self.request.POST.get('reject')
        # reject=request.session[id]
    if model == 2:
        ram = ApplicationsModel.objects.get(id=id)
        ram.reject_status=1
        ram.save()
        # reject = self.request.POST.get('reject')
        # reject=request.session[id]
    if model == 3:
        rbm = BookingsModel.objects.get(id=id)
        rbm.reject_status=1
        rbm.save()
        # reject=self.request.POST.get('reject')
        # reject=request.session[id]
    return HttpResponseRedirect('/manager')

def accept(request,id,model):
    if model == 1:
        apm =ProductsModel.objects.get(id=id)
        apm.accept_status=1
        apm.save()
        # accept=self.request.POST.get('accept')
        # accept = request.session[id]
    if model == 2:
        aam=ApplicationsModel.objects.get(id=id)
        aam.accept_status=1
        aam.save()
        # accept=self.request.POST.get('accept')
        # accept=request.session[id]
    if model == 3:
        abm=BookingsModel.objects.get(id=id)
        abm.accept_status=1
        abm.save()
        # accept=self.request.POST.get('accept')
        # accept=request.session[id]
    return HttpResponseRedirect('/manager')

def admin(request):
    pfm=ProductsModel.objects.all()
    afm=ApplicationsModel.objects.all()
    bfm=BookingsModel.objects.all()
    id = 'pending'
    print(pfm)
    print(afm)
    print(bfm)
    if pfm=='1':
            id.replace('reject')
    if afm=='1':
            id.replace('reject')
    if bfm == '1':
            id.replace('reject')
    context={'pfm':pfm,'afm':afm,'bfm':bfm,'id':id}
    return render(request,'admin.html', context )
