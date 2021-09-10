from django.urls import path

from .views import book_a_ride_view, riders_list_view, ride_service_type_list_view, ride_service_type_detail_view

urlpatterns = [
    path('book_a_ride/<service_type_id>', book_a_ride_view, name='book_a_ride'),
    path('riders_list/', riders_list_view, name='riders_list'),
    path('ride_service_type/', ride_service_type_list_view, name='ride_service_type'),
    path('ride_service_type_detail/<id>/', ride_service_type_detail_view, name='ride_service_type_detail'),
]