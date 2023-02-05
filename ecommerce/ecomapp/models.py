from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class registermodel(models.Model):
    username=models.CharField(max_length=25)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.email

class shopmodel(models.Model):
    shopname=models.CharField(max_length=35)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.shopname

class uploadmodel(models.Model):
    productname=models.CharField(max_length=25)
    price=models.CharField(max_length=25)
    description=models.CharField(max_length=25)
    image=models.ImageField(upload_to="ecomapp/static")
    def __str__(self):
        return self.productname

class cartmodel(models.Model):
    productname=models.CharField(max_length=25)
    price=models.CharField(max_length=25)
    description=models.CharField(max_length=25)
    image=models.ImageField(upload_to="ecomapp/static")
    def __str__(self):
        return self.price


# ---------------------------------------------------------------------------------------------------------------------------------------------

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.user