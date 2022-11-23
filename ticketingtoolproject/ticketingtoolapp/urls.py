from django.urls import path 

from . import views 

urlpatterns = [
    path("",views.home,name="homepage"),
    path("employee",views.employee,name='employee'),
    path("manager",views.manager,name='manager'),
    path("adminpage",views.admin,name='admin'),
    path('login',views.login,name="logpage"),
<<<<<<< HEAD
    path('products',views.products,name='products'),
    path('application',views.application,name='application'),
    path('booking',views.booking,name='booking'),
=======
    path('sign/',views.signup,name="signup"),
>>>>>>> 1f6d5f4364bed3e7548ac19bf8ed6826a19c2c69
]




