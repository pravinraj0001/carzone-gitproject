from django.shortcuts import render
from .models import Team

# Create your views here.
def home(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
            'teams': teams,
    }
    return render(request, 'pages/about.html', data) # Change PR01003

def services(request):
    return render(request, 'pages/services.html') # Change PR01003

def contact(request):
    return render(request, 'pages/contact.html') # Change PR01003
