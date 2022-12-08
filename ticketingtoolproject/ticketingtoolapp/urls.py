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
    path('stationary',views.stationary,name='stationary'),

    path('sign/',views.signup,name="signup"),
    path('logout/',views.ulogout,name="logout"),
    # path('delete/<int:id>/<int:model>',views.tdelete,name='delete'),
    path('accept/<int:id>/<int:model>',views.accept,name='accept'),
    path('reject/<int:id>/<int:model>',views.reject,name='reject'),
]




