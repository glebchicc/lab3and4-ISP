from django.shortcuts import render
from .models import Bus, Passanger


def index(request):
    nearest_buses = Bus.objects.order_by("-departure_time")
    return render(request, 'hello/buses.html', {'nearest_buses': nearest_buses})
