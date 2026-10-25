from django.shortcuts import render
from .models import Team
from cars.models import Car #PR01009 - Featured Cars Dashboard

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True) #PR01009 - Featured Cars Dashboard
    all_cars = Car.objects.order_by('-created_date')
    data = {
        'teams': teams,
        'featured_cars': featured_cars, #PR01009 - Featured Cars Dashboard
        'all_cars': all_cars, #PR01009 - Featured Cars Dashboard
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
