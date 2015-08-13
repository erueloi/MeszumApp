from django.shortcuts import render

def index(request):
    context_dict = {}
    return render(request, 'index.html', context_dict)

def login(request):

    context_dict = {}
    return render(request, 'login.html', context_dict)

def administrationspace(request):
    context_dict = {}
    return render(request, 'AdministrationSpace.html', context_dict)