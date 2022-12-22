from django.contrib import admin

# import your models here
from .models import Truck, Service, Mod

# Register your models here
admin.site.register(Truck)
admin.site.register(Service)
admin.site.register(Mod)