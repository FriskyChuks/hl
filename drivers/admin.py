from django.contrib import admin

from .models import CarOwnerDriverRegister, BankAccountInformation, DriverRequest

admin.site.register(CarOwnerDriverRegister)
admin.site.register(BankAccountInformation)
admin.site.register(DriverRequest)
