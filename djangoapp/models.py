from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime



# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description  = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake,on_delete=models.CASCADE,related_name='models')
    name = models.CharField(max_length=100)
    dealer_id = models.IntegerField()
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
    ]
    type = models.CharField(max_length=10,choices=CAR_TYPES,default='SUV')
    year = models.DateField()
    color = models.CharField(max_length=100,null=True,blank=True)
    horspepower = models.IntegerField(null=True,blank=True)
    
    
    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.type})"
   

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
