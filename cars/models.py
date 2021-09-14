from django.db import models
from django.utils import timezone

from accounts.models import User

MAINTENANCE_TYPE = (
    ('routine','Routine'),
    ('others','Others'),
)


class RideServiceClass(models.Model):
    service_class = models.CharField(max_length=20)
    date_created  = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated       = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.service_class


class CarBrand(models.Model):
    brand = models.CharField(max_length=50) 
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.brand


class Car(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="image/", default='image/male.jpg')
    plate_no = models.CharField(max_length=12)
    chasis_no = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    service_class = models.ForeignKey(RideServiceClass, on_delete=models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE, blank=True, null=True)
    active = models.BooleanField(default=True)
    is_booked = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.model}"


class CarReservation(models.Model):
    check_in = models.DateField(default=timezone.now)
    check_out = models.DateField()
    car = models.ForeignKey(Car, on_delete = models.CASCADE)
    rider = models.ForeignKey(User, on_delete= models.CASCADE)


class VehicleMaintenance(models.Model):
    car             = models.ForeignKey(Car, on_delete=models.CASCADE)
    user            = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    type            = models.CharField(max_length=20, choices=MAINTENANCE_TYPE)
    date_maintained = models.DateField()
    amount_spent    = models.DecimalField(max_digits=65, decimal_places=2, default=00.00)
    description     = models.TextField(max_length=500)
    date_created    = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return f"{self.car}; Amount Spent: {self.amount_spent}"



