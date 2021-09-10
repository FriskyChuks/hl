from django.contrib.messages.api import success
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from accounts.models import User

from .models import Car, RideServiceClass


def car_class_view(request, id):
    car_class = Car.objects.filter(service_class_id=id,active=True)
    # car_executive = RideServiceClass.objects.get(id=1)
    # car_luxury = RideServiceClass.objects.get(service_class=2,active=True)
    # car_comfort = RideServiceClass.objects.get(service_class=3,active=True)
    print("class is:")

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



