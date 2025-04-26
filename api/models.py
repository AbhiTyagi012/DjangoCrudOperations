from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=50)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.make} {self.model}"


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    license_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.customer.name} booked {self.car.make}"






# API endpoints for CRUD operations on all models
 
# Endpoint to get available cars for a date range
 
# Validate that a car cannot be double-booked

 
