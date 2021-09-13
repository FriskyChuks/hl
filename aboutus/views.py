from django.shortcuts import render

from riders.models import ServiceType

def about_us_view(request):
    services = ServiceType.objects.all()

    return render(request, 'aboutus/about_us.html', {"services":services})


def contact_us_view(request):
    services = ServiceType.objects.all()

    return render(request, 'aboutus/contact_us.html', {"services":services})

