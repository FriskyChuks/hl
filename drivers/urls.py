from django.urls import path

from .views import (
    car_owners_and_drivers_view,
    bank_account_info_view,
    driver_request_view,
    pending_drivers_request_view,
    drivers_request_detail_view,
    sit_back_and_earn_view
)     

urlpatterns = [
    path("car_owners_and_drivers/", car_owners_and_drivers_view, name="car_owners_and_drivers"),
    path("bank_account_info/<user_id>/", bank_account_info_view, name="bank_account_info"),
    path("driver_request/", driver_request_view, name="driver_request"),
    path("sit_back_and_earn/", sit_back_and_earn_view, name="sit_back_and_earn"),
    path("pending_driver_request/", pending_drivers_request_view, name="pending_driver_request"),
    path("approve_drivers_request/<id>", drivers_request_detail_view, name="approve_drivers_request")
]