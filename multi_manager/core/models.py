from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from .managers import TenantManager,TenantUserManager

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)

class Company(models.Model):
    name = models.CharField(max_length=255)
    models.ForeignKey("Customer", on_delete=models.CASCADE)    
    def __str__(self) -> str:
        return self.name

class User(AbstractUser):
    companies = models.ManyToManyField('Company')
    admin_objects=UserManager()
    objects=TenantUserManager()
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    company=models.ForeignKey('Company',on_delete=models.CASCADE)
    objects=TenantManager()

    def __str__(self) -> str:
        return self.name