from django.db import models

# Create your models here.
products=(('bag','Bag'),('laptop','Laptop'),('mouse','Mouse'),('headset','Headset'),('keyboard','Keyboard'),('other','Other'))
class ProductsModel(models.Model):
    employee_id=models.IntegerField(default=00000)
    employee_name=models.CharField(max_length=100,default="XXXXXXXXX")
    Products = models.CharField (max_length=100,choices=products, default='other')
    Reason=models.TextField()
    def __str__(self):
        return str(self.Products)

application=(('pycharm','Pycharm'),('vscode','VSCode'),('python','Python'),('java','Java'),('mysql','MySql'),('ecllipse','Ecllipse'),('other','Other'))
class ApplicationsModel(models.Model):
    employee_id=models.IntegerField(default=00000)
    employee_name=models.CharField(max_length=100,default="XXXXXXXXX")
    application = models.CharField(max_length=100, choices=application, default='other')
    Reason=models.TextField()
    def __str__(self):
        return str(self.application)

booking=(('cubical','Cubical'),('training room','Training Room'),('board room','Board Room'),('interview room','Interview Room'),('other','Other'))
class BookingsModel(models.Model):
    employee_id=models.IntegerField(default=00000)
    employee_name=models.CharField(max_length=100,default="XXXXXXXXX")
    booking = models.CharField( max_length=100,choices=booking, default='other')
    Reason=models.TextField()
    def __str__(self):
        return str(self.booking)
        

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

