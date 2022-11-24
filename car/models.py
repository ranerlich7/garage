from django.db import models

class Car(models.Model):
    class CarType(models.TextChoices):
        CAR = 'C', 'Car'
        TRUCK = 'T', 'Truck'
        MOTORCYCLE = 'M', 'Motorcycle'

    cartype = models.CharField(max_length=3, choices=CarType.choices, default=CarType.CAR)
    number = models.CharField(max_length=20, null=False)
    manufacturer = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True,
                              default='car.png')

