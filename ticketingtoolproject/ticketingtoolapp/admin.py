from django.contrib import admin
from .models import ProductModel,ApplicationModel,BookingModel
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