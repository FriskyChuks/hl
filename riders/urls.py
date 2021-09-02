from django.urls import path

from .views import book_a_ride_view, riders_list_view

urlpatterns = [
    path('book_a_ride', book_a_ride_view, name='book_a_ride'),
    path('riders_list', riders_list_view, name='riders_list'),
]