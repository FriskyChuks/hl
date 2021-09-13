from django.contrib import admin

from .models import CarOwnerDriverRegister, BankAccountInformation, DriverRequest#, SitBackAndEarn

admin.site.register(CarOwnerDriverRegister)
admin.site.register(BankAccountInformation)
admin.site.register(DriverRequest)
# admin.site.register(SitBackAndEarn)
