from django.contrib import admin

from .models import CarBrand, Car, CarOwnerDriverRegister, RideServiceClass, BankAccountInformation


admin.site.register(Car)
admin.site.register(CarBrand)
admin.site.register(CarOwnerDriverRegister)
admin.site.register(RideServiceClass)
admin.site.register(BankAccountInformation)
