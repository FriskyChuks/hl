# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("accounts.urls")), # Auth routes - login / register
    path("cars/", include("cars.urls")),            # Cars route
    path("riders/", include("riders.urls"))
    # path("app", include("app.urls"))             # UI Kits Html files
]
