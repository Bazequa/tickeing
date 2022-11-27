from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.
products=(('bag','Bag'),('laptop','Laptop'),('mouse','Mouse'),('headset','Headset'),('keyboard','Keyboard'),('other','Other'))
class ProductModel(models.Model):
    Products = models.CharField (max_length=100,choices=products, default='other')
    Reason=models.TextField()

application=(('pycharm','Pycharm'),('vscode','VSCode'),('python','Python'),('java','Java'),('mysql','MySql'),('ecllipse','Ecllipse'),('other','Other'))
class ApplicationModel(models.Model):
    application = models.CharField(max_length=100, choices=application, default='other')
    Reason=models.TextField()

booking=(('cubical','Cubical'),('training room','Training Room'),('board room','Board Room'),('interview room','Interview Room'),('other','Other'))
class BookingModel(models.Model):
    booking = models.CharField( max_length=100,choices=booking, default='other')
    Reason=models.TextField()

roles = [('Manager','Manager'),('Employee','Employee'),('UserAdmin','UserAdmin')]
class User(models.Model):
    username=models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    role = models.CharField(max_length=100,choices=roles)
    password = models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)

# class Org(AbstractUser):
#      is_admin= models.BooleanField('Is admin', default=False)
#      is_customer = models.BooleanField('Is customer', default=False)
#      is_employee = models.BooleanField('Is employee', default=False)


# class Employee(models.Model):
#     ename=models.CharField(max_length=100)
#     epassword=models.SlugField(max_length=100)


# class Manager(models.Model):
#     mname=models.CharField(max_length=100)
#     mpassword=models.SlugField(max_length=100)


# class AdminPage(models.Model):
#     aname=models.CharField(max_length=100)
#     apassword=models.SlugField(max_length=100)

