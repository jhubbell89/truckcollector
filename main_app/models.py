from django.db import models
from django.urls import reverse

# Create your models here.
class Truck(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    condition = models.TextField(max_length=250)
    year = models.IntegerField()

    def __str__(self):
      return self.model

    def get_absolute_url(self):
      return reverse('detail', kwargs={'truck_id': self.id})
