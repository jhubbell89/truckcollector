from django.contrib import admin

# import your models here
from .models import Truck, Service

# Register your models here
admin.site.register(Truck)
admin.site.register(Service)
