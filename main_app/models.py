from django.db import models
from django.urls import reverse
from datetime import date

WEEKLYCHECK = (
  ('T', 'Tire Pressure'),
  ('E', 'Engine Oil Level'),
  ('M', 'Mirrors'),
  ('L', 'Lights')
)

class Mod(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
      return self.name

    def get_absolute_url(self):
      return reverse('mods_detail', kwargs={'pk': self.id})

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

    def fed_for_today(self):
      return self.service_set.filter(date=date.today()).count() >= len(WEEKLYCHECK)

class Service(models.Model):
    date = models.DateField('Service Date')
    weeklychecks = models.CharField('Weekly Checks', max_length=1, choices=WEEKLYCHECK, default=WEEKLYCHECK[0][0])

    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)

    def __str__(self):
      return f"{self.get_weeklychecks_display()} on {self.date}"

    class Meta:
      ordering = ['-date']