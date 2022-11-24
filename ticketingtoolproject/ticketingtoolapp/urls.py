from django.urls import path 

from . import views 

urlpatterns = [
    path("",views.home,name="homepage"),
    path("employee",views.employee,name='employee'),
    path("manager",views.manager,name='manager'),
    path("adminpage",views.admin,name='admin'),
    path('login/',views.user_login,name="logpage"),

    path('products',views.products,name='products'),
    path('application',views.application,name='application'),
    path('booking',views.booking,name='booking'),

    path('sign/',views.signup,name="signup"),
    path('',views.logout,name="logout"),
]




