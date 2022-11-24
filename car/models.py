from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    class CarType(models.TextChoices):
        CAR = 'C', 'CAR'
        TRUCK = 'T', 'TRUCK'
        MOTORCYCLE = 'M', 'MOTORCYCLE'

    cartype = models.CharField(max_length=3, choices=CarType.choices, default=CarType.CAR)
    number = models.CharField(max_length=20, null=False)
    manufacturer = models.CharField(max_length=20)


class Employee(User):
    tagnumber = models.CharField(max_length=50)

class Treatment(models.Model):
    class TreatmentType(models.IntegerChoices):
        TEN_TOUSAND = 1, '10,000'
        BREAKS = 2, 'BREAKS'
        THIRTY_THOUSAND = 3, '30,000'
        
    type = models.IntegerField(choices=TreatmentType.choices, null=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)




