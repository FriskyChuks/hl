from django.contrib.messages.api import success
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from accounts.models import User

from .models import Car, RideServiceClass, VehicleMaintenance
from .forms import VehicleMaintenanceForm


def car_class_view(request, id):
    car_class = Car.objects.filter(service_class_id=id,active=True)
 
    template = 'cars/service_class_list.html'
    context = {"car_class":car_class}
    return render(request, template, context)


def car_list_view(request):
    cars = Car.objects.filter(active=True)
    template = 'cars/car_list.html'
    context = {"cars":cars}
    return render(request, template, context)


def car_detail_view(request, id):
    car = Car.objects.get(id=id, active=True)
    template = 'cars/car_detail.html'
    context = {"car":car}
    return render(request, template, context)


@login_required
def vehicle_maintenance_view(request):
    form = VehicleMaintenanceForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Maintenance record saved successfully!")
        return redirect("/cars/maintenance")

    return render(request, 'cars/maintenance.html', {"form":form})

@login_required
def maintenance_report_view(request, user_id):
    all_maintenance = VehicleMaintenance.objects.all()
    user_maintenance = VehicleMaintenance.objects.filter(user=user_id)

    context = {"all_maintenance":all_maintenance, "user_maintenance":user_maintenance}
    return render(request, 'cars/maintenance_report.html', context)