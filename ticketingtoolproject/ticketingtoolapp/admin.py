from django.contrib import admin
from ticketingtoolapp.models import ProductModel,ApplicationModel,BookingModel,Employee,Manager,AdminPage
# from ticketingtoolapp.models import Org
# Register your models here.
@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    include='__all__'

@admin.register(ApplicationModel)
class ApplicationAdmin(admin.ModelAdmin):
    include='__all__'

@admin.register(BookingModel)
class BookingAdmin(admin.ModelAdmin):
    include='__all__'

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    include='__all__'

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    include='__all__'

@admin.register(AdminPage)
class AdminPageAdmin(admin.ModelAdmin):
    include='__all__'

# admin.site.register(Org)