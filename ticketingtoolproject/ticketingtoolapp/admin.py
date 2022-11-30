from django.contrib import admin
from ticketingtoolapp.models import ProductsModel,ApplicationsModel,BookingsModel
# from ticketingtoolapp.models import Employee,Manager,AdminPage
# from ticketingtoolapp.models import Org
# Register your models here.

@admin.register(ProductsModel)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id','employee_id','employee_name','Products','Reason']

@admin.register(ApplicationsModel)
class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ['id','employee_id','employee_name','application','Reason']

@admin.register(BookingsModel)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ['id','employee_id','employee_name','booking','Reason']



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

