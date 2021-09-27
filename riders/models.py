from django.db import models
from django.urls import reverse

from accounts.models import User
from cars.models import Car, RideServiceClass


RIDE_STATUS = (
    ('1','pending'),
    ('2','arriving'),
    ('3','active'),
    ('4','done')
)


class ServiceType(models.Model):
    service_type = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="cars/", default="cars/1.jpg")
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.service_type
    
    def get_absolute_url(self):       
        return reverse('ride_service_type_detail', args=[str(self.id)])


class Ride(models.Model):
    rider           = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    # car             = models.ForeignKey(Car, blank=True, null=True, on_delete=models.CASCADE)
    pickup_address  = models.CharField(max_length=255, blank=True, null=True)
    destination     = models.CharField(max_length=255)
    distance        = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    service_class   = models.ForeignKey(RideServiceClass, on_delete=models.CASCADE)
    service_type    = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    comments		= models.TextField(max_length=500)
    status          = models.CharField(max_length=1, choices=RIDE_STATUS, default=1)
    ride_date       = models.DateField()
    ride_time       = models.TimeField()
    date_created    = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated         = models.DateTimeField(auto_now_add=False, auto_now=True)

    # def __str__(self):
    #     return f"{self.rider.first_name} {self.rider.last_name}"

