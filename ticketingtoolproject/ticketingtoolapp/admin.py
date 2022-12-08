from django.contrib import admin
from ticketingtoolapp.models import ProductModel,ApplicationModel,BookingModel,StationaryModel
# from ticketingtoolapp.models import Employee,Manager,AdminPage
# from ticketingtoolapp.models import Org
# Register your models here.

@admin.register(ProductModel)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id','employee_id','employee_name','your_requirement','Reason','request_raised_at']

@admin.register(ApplicationModel)
class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ['id','employee_id','employee_name','your_requirement','Reason','request_raised_at']

@admin.register(BookingModel)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ['id','employee_id','employee_name','your_requirement','Reason','request_raised_at']

@admin.register(StationaryModel)
class StationaryAdmin(admin.ModelAdmin):
    list_display = ['id','employee_id','employee_name','your_requirement','Reason','request_raised_at']

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

