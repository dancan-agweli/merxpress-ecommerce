from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class SignUp(models.Model):
    username=models.CharField(max_length=50) #Noo Need we will use email as username and primary key
    email=models.EmailField(max_length=50,primary_key=True)
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    dob = models.DateField() # helps for further in ml for user suggestion
    #gender = models.CharField(max_length = 10) Optional field for user
    phone=models.BigIntegerField()
    password=models.CharField(max_length=10)
    confirm_password=models.CharField(max_length=10) #No need of it we just have to compare it while taking input NO NEED THIS FIELD
    
# order page models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('placed', 'Placed'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')])

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Cancellation(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Return(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Refund(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
