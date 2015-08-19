from django.shortcuts import render
from django.contrib import messages
from meszum.forms import SpaceForm, EventForm
from meszum.models import Space
from django.contrib.auth.models import User

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
    return render(request, 'admin/events.html', context_dict)

def addevents(request):

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            #Save Event
            messages.add_message(request, messages.SUCCESS, 'S''ha guardat correctament')
        else:
            print form.errors
    else:
        form = EventForm()

    return render(request, 'admin/addevents.html', {'form': form})