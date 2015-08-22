from django.shortcuts import render
from django.contrib import messages
from meszum.forms import SpaceForm, EventForm
from meszum.models import Space, Event
from django.contrib.auth.models import User
from geopy.geocoders.googlev3 import GoogleV3
from geopy.geocoders.googlev3 import GeocoderQueryError
from urllib2 import URLError
from django.contrib.gis import geos

def geocode_address(address):
    address = address.encode('utf-8')
    geocoder = GoogleV3()
    try:
        _, latlon = geocoder.geocode(address)
    except (URLError, GeocoderQueryError, ValueError):
        return None
    else:
        point = "POINT(%s %s)" % (latlon[1], latlon[0])
        return geos.fromstr(point)

def index(request):
    context_dict = {}
    return render(request, 'index.html', context_dict)

def login(request):

    context_dict = {}
    return render(request, 'login.html', context_dict)

def administrationspace(request):

    objUser = User.objects.get(id=request.user.id)
    try:
        objSpace = Space.objects.get(user=objUser)
    except Space.DoesNotExist:
        objSpace = None

    # A HTTP POST?
    if request.method == 'POST':
        form = SpaceForm(request.POST, instance=objSpace)
        if form.is_valid():
            objSpace = form.save(commit=False)
            objSpace.user = objUser
            objSpace.save()
            messages.add_message(request, messages.SUCCESS, 'S''ha guardat correctament')
            #return redirect('administrationspace')
        else:
            print form.errors
    else:
        form = SpaceForm(instance=objSpace)

    return render(request, 'admin/space.html', {'form': form})

def administrationevents(request):
    context_dict = {}

    try:
        space = Space.objects.get(user=request.user.id)
        events = Event.objects.filter(space=space).order_by('startdate')
    except Space.DoesNotExist:
        space = None
        events = None

    context_dict['association'] = space
    context_dict['events'] = events

    return render(request, 'admin/events.html', context_dict)

def addevents(request):
    objUser = User.objects.get(id=request.user.id)
    try:
        objSpace = Space.objects.get(user=objUser)
    except Space.DoesNotExist:
        objSpace = None

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            address = form.cleaned_data['address']
            objEvent = form.save(commit=False)
            objEvent.geometry = geocode_address(address)
            objEvent.space = objSpace
            objEvent.save()
            #Save Event
            messages.success(request,'S''ha guardat correctament l''Event')
            return administrationevents(request)
        else:
            print form.errors
    else:
        form = EventForm()

    return render(request, 'admin/addevents.html', {'form': form})