from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name



class Barbershop(models.Model):
    CATEGORY = (
        ('Only haircuts','Only haircuts'),
        ('all services','all services'),
        )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    Barbershopname = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    area = models.CharField(max_length=100, null=True)
    service = models.CharField(max_length=100, null=True, choices=CATEGORY)


    def __str__(self):
        return self.Barbershopname

class Book(models.Model):
    STATUS = (
        ('Haircut and Shaving 10$','Haircut and Shaving 10$'),
        ('Haircut and Trimming 8$','Haircut and Trimming 8$' ),
        ('Haircut 7$','Haircut 7$' ),
        )
    TIME = (
        ('Morning','Morning'),
        ('Lunch Time','Lunch Time'),
        ('Evening','Evening'),
        ('Night', 'Night'),
        )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    barbershop = models.ForeignKey(Barbershop, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    time = models.CharField(max_length=200, null=True, choices=TIME)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
