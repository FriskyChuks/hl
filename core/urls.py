# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("accounts.urls")),
    path('accounts/', include('accounts.password.urls')), # Passwords
    path("cars/", include("cars.urls")), 
    path("driverss/", include("drivers.urls")),           # Cars route
    path("riders/", include("riders.urls"))
    # path("app", include("app.urls"))             # UI Kits Html files
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
