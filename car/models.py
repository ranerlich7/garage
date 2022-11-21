from django.db import models

class Car(models.Model):
    class CarType(models.TextChoices):
        CAR = 'C', 'CAR'
        TRUCK = 'T', 'TRUCK'
        MOTORCYCLE = 'M', 'MOTORCYCLE'

    cartype = models.CharField(max_length=3, choices=CarType.choices, default=CarType.CAR)
    number = models.CharField(max_length=20, null=False)
    manufacturer = models.CharField(max_length=20)

