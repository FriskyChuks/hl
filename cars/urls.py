from django.urls import path

from .views import (
    car_list_view,
    car_class_view,
    car_owners_and_drivers_view,
    bank_account_info_view,
    driver_request_view
)     

urlpatterns = [
    path("car_list/", car_list_view, name="car_list"),
    path("car_class/<id>/", car_class_view, name="car_class"),
    path("car_owners_and_drivers/", car_owners_and_drivers_view, name="car_owners_and_drivers"),
    path("bank_account_info/<user_id>/", bank_account_info_view, name="bank_account_info"),
    path("driver_request/", driver_request_view, name="driver_request")
]