from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
priority=(('high','High'),('medium','Medium'),('low','Low'))

product=(('laptop','Laptop'),('mouse','Mouse'),('headset','Headset'),('keyboard','Keyboard'),('other','Other'))
class ProductModel(models.Model):
    employee_id=models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    employee_name=models.CharField(max_length=100,null=True)
    priority=models.CharField(max_length=100,choices=priority,default='low')
    your_requirement = models.CharField (max_length=100,choices=product,default='Other')
    Reason=models.TextField()
    request_raised_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.Products)

application=(('pycharm','Pycharm'),('vscode','VSCode'),('python','Python'),('java','Java'),('mysql','MySql'),('ecllipse','Ecllipse'),('other','Other'))
class ApplicationModel(models.Model):
    employee_id=models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    employee_name=models.CharField(max_length=100,null=True)
    priority=models.CharField(max_length=100,choices=priority,default='low')
    your_requirement = models.CharField(max_length=100, choices=application,default='Other')
    Reason=models.TextField()
    request_raised_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.application)

booking=(('cubical','Cubical'),('training room','Training Room'),('board room','Board Room'),('interview room','Interview Room'),('other','Other'))
class BookingModel(models.Model):
    employee_id=models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    employee_name=models.CharField(max_length=100,null=True)
    priority=models.CharField(max_length=100,choices=priority,default='low')
    your_requirement = models.CharField( max_length=100,choices=booking,default='Other')
    Reason=models.TextField()
    request_raised_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.booking)
        
stationary=(('bag','Bag'),('pen','Pen'),('pencil','Pencil'),('paper','Paper'),('stapler','Stapler'),('book','Book'),('other','Other'))
class StationaryModel(models.Model):
    employee_id=models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    employee_name=models.CharField(max_length=100,null=True)
    priority=models.CharField(max_length=100,choices=priority,default='low')
    your_requirement = models.CharField( max_length=100,choices=stationary,default='Other')
    Reason=models.TextField()
    request_raised_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.stationary)








# roles = [('Manager','Manager'),('Employee','Employee'),('UserAdmin','UserAdmin')]
# class User(models.Model):
#     username=models.CharField(max_length=100)
#     first_name = models.CharField(max_length=100)
#     second_name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     role = models.CharField(max_length=100,choices=roles)
#     password = models.CharField(max_length=100)
#     confirm_password=models.CharField(max_length=100)
#     def __str__(self):
#         return self.username




# class Employee(models.Model):
#     ename=models.CharField(max_length=100)
#     epassword=models.SlugField(max_length=100)


# class Manager(models.Model):
#     mname=models.CharField(max_length=100)
#     mpassword=models.SlugField(max_length=100)


# class AdminPage(models.Model):
#     aname=models.CharField(max_length=100)
#     apassword=models.SlugField(max_length=100)

