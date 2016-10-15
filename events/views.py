from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

def locations(request):
    locations = Location.objects.all()
    return render(request, 'locations.html', {'locations': locations})
def home(request):
    return render(request, 'index.html')
def business(request, pk):
    location = get_object_or_404(Location, pk=pk)
    return render(request, 'business.html', {'location': location})
def event_details(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event_details.html', {'event': event})
