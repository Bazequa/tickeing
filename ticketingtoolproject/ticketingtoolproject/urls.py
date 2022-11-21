"""ticketingtoolproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('',include('ticketingtoolapp.urls'))
    
=======
    path("",views.home),
    path("employee",views.employee,name='employee'),
    path("manager",views.manager,name='manager'),
    path("adminpage",views.admin,name='admin'),
<<<<<<< HEAD
    path('products',views.products,name='products'),
    path('application',views.application,name='application'),
    path('booking',views.booking,name='booking'),
=======
>>>>>>> c147e47373e2a6b5134d338d609dcfe42fa4e3dd
>>>>>>> ea5ccdeef800799cad01859117770b7fe74ab5a6
]
