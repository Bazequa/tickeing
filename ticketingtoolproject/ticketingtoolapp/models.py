from django.db import models

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

<<<<<<< HEAD
class Employee(models.Model):
    pass
class Manager(models.Model):
    pass
class AdminPage(models.Model):
    pass
=======
# class Singup()
>>>>>>> 1f6d5f4364bed3e7548ac19bf8ed6826a19c2c69
