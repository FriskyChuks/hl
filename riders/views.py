from django.shortcuts import redirect, render, HttpResponseRedirect
# import geoip2.database
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import folium
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
import json

from accounts.models import User
from .models import Ride, ServiceType
from .forms import BookRideForm
from .utils import get_geo, get_center_coordinates, get_zoom, get_ip_address


# @login_required
def book_a_ride_view(request, service_type_id):
    service = ServiceType.objects.get(id=service_type_id)
    user_id = request.user.id
    
    if request.method == 'POST':
        pickup_address = request.POST.get('pickup_address')
        destination=request.POST.get('destination')
        service_class = request.POST.get('service_class')
        ride_date = request.POST.get('ride_date')
        ride_time = request.POST.get('ride_time')
        comments = request.POST.get('comments')
        # request.session['pickup_address'] = pickup_address
        # request.session['destination'] = destination
        # request.session['service_class'] = service_class
        # request.session['ride_date'] = ride_date
        # request.session['ride_time'] = ride_time
        # request.session['comments'] = comments
        # print(request.session['pickup_address'])
        form_obj = Ride.objects.create(
            rider_id = user_id,
            pickup_address = pickup_address,
            destination=destination,
            service_class_id = service_class,
            service_type_id=service_type_id,
            ride_date=ride_date,
            ride_time=ride_time,
            comments = comments
        )
        form_obj.save()
        messages.success(request, 'Your booking was successful')
        return redirect('/')
        # if not request.user.is_authenticated:
        #     messages.info(request, 'Please kindly login to continue')
        #     return HttpResponseRedirect('/login/?next=%s' % request.path)
        # else:
        #     form_obj.save()
        #     messages.success(request, 'Your booking was successful')
        #     return redirect('/')
   
    template = 'riders/book_ride.html'
    context = {"service":service}
    return render(request, template, context)


@login_required
def riders_list_view(request):
    pending_riders = Ride.objects.filter(status=1)# Pending riders
    active_riders = Ride.objects.filter(status=3)# Active Riders
    # print(riders)

    template = 'riders/riders_list.html'
    context = {"pending_riders":pending_riders, "active_riders":active_riders}
    return render(request, template, context)


def ride_service_type_list_view(request):
    services = ServiceType.objects.filter(active=True)

    return render(request, 'riders/ride_service.html', {"services":services})


def ride_service_type_detail_view(request, id):
    service = ServiceType.objects.get(id=id)

    return render(request, 'riders/ride_service_details.html', {"service":service})


def my_rides_view(request, user_id):
    pending_rides = Ride.objects.filter(rider=user_id, status=1)
    active_rides = Ride.objects.filter(rider=user_id, status=3)

    template = 'riders/user_rides.html'
    context = {"pending_rides":pending_rides, "active_rides":active_rides}
    return render(request, template, context)



