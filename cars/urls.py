from django.urls import path

from .views import (
    car_list_view,
    car_class_view,
    vehicle_maintenance_view,
    maintenance_report_view
)     

urlpatterns = [
    path("car_list/", car_list_view, name="car_list"),
    path("car_class/<id>/", car_class_view, name="car_class"),
    path("maintenance/", vehicle_maintenance_view, name="maintenance"),
    path("maintenance_report/<user_id>/", maintenance_report_view, name="maintenance_report"),
]