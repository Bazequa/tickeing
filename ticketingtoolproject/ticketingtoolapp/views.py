from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def employee(request):
    return render(request,'employee.html')
def manager(request):
    return render(request,'manager.html')
def admin(request):
    return render(request,'admin.html')

def login(request):
    return render(request,'login.html')
