from django.shortcuts import render
from django.http import HttpResponse
from .models import City

def index(request):
    cities = City.objects.all()

    return render(request, 'cities.html', {'cities': cities})

def get_city(request, id):
    city = City.objects.get(id=id)

    return render(request, 'city.html', {'city': city})
