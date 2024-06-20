from django.db import models

# Create your models here.
class SignUp(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50,primary_key=True)
    phone=models.BigIntegerField()
    password=models.CharField(max_length=10)
    confirm_password=models.CharField(max_length=10)


