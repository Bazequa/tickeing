from django.contrib import admin
from ticketingtoolapp.models import ProductModel,ApplicationModel,BookingModel
# from ticketingtoolapp.models import Employee,Manager,AdminPage
# from ticketingtoolapp.models import Org
# Register your models here.

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','Products','Reason']

@admin.register(ApplicationModel)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id','application','Reason']

@admin.register(BookingModel)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id','booking','Reason']



# @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     include='__all__'
#
# @admin.register(Manager)
# class ManagerAdmin(admin.ModelAdmin):
#     include='__all__'
#
# @admin.register(AdminPage)
# class AdminPageAdmin(admin.ModelAdmin):
#     include='__all__'

