from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Change PR01002
    path('about', views.about, name='about'), # Change PR01003
    path('services', views.services, name='services'), # Change PR01003
    path('contact', views.contact, name='contact'), # Change PR01003
]