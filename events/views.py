from django.shortcuts import render
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
