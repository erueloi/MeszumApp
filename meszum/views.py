from django.shortcuts import render
from meszum.forms import SpaceForm
from django.contrib.auth.models import User

def index(request):
    context_dict = {}
    return render(request, 'index.html', context_dict)

def login(request):

    context_dict = {}
    return render(request, 'login.html', context_dict)

def administrationspace(request):

    objUser = User.objects.get(user=request.user)

    # A HTTP POST?
    if request.method == 'POST':
        form = SpaceForm(request.POST)

        if form.is_valid():
            objSpace = form.save(commit=False)
            objSpace.user = objUser
            objSpace.save()

            return administrationspace(request)
        else:
            print form.errors
    else:
        form = SpaceForm()

    return render(request, 'AdministrationSpace.html', {'form': form})

def administrationevents(request):
    context_dict = {}
    return render(request, 'AdministrationEvents.html', context_dict)