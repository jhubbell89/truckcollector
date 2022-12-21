from django.db import models

# Create your models here.
class Truck(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    condition = models.TextField(max_length=250)
    year = models.IntegerField()

    def __str__(self):
      return self.name
