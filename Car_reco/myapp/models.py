from django.db import models

from django.db import models

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.DecimalField(max_digits=5, decimal_places=2)
    seating_capacity = models.IntegerField()
    image_url = models.URLField(max_length=200)
    car = models.CharField(max_length=100)
    transmission = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50)

    def __str__(self):
        return self.car

