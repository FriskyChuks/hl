from django.shortcuts import redirect, render
# import geoip2.database
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import folium
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Ride
from .forms import BookRideForm
from .utils import get_geo, get_center_coordinates, get_zoom, get_ip_address


@login_required
def book_a_ride_view(request):
    form = BookRideForm(request.POST or None)
    msg = ""
    if form.is_valid():
        new_form = form.save(commit=False)
        # destination_ = form.cleaned_data.get('destination')
        new_form.rider_id = request.user.id
        new_form.save()
        messages.success(request, 'Your booking was successful')
        return redirect('book_a_ride')
   
    template = 'riders/book_ride.html'
    context = {"form":form, "msg":msg}
    return render(request, template, context)



def riders_list_view(request):
    pending_riders = Ride.objects.filter(status=1)# Pending riders
    active_riders = Ride.objects.filter(status=3)# Active Riders
    # print(riders)

    template = 'riders/riders_list.html'
    context = {"pending_riders":pending_riders, "active_riders":active_riders}
    return render(request, template, context)


