from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    
    CHOICES= (
        ('A', 'Automatic'),
        ('M', 'Manuel'),
    )
    
    plate_number = models.CharField(max_length=15, unique=True)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.SmallIntegerField()
    gear = models.CharField(max_length=20, choices=CHOICES,default="M")
    rent_per_day = models.IntegerField()
    availability = models.BooleanField(default=True)
    
    def __str__(self) :
        return f"{self.brand} - {self.model} - {self.plate_number} - {self.rent_per_day}"
    
    class Meta:
        verbose_name_plural = "Carss"
        ordering = ['brand']
        

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.user.username
    
    
class Reservation(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    