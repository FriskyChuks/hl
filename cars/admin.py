from django.contrib import admin

from .models import CarBrand, Car, RideServiceClass


admin.site.register(Car)
admin.site.register(CarBrand)
admin.site.register(RideServiceClass)

