from django.shortcuts import render
from .models import Desinations

# Create your views here.

def home(request):
    # dest1 = Desinations()
    # dest1.country = 'United States'
    # dest1.image = 'country-1.jpg'
    # dest1.cities = 5
    # dest1.price = 1500

    # dest2 = Desinations()
    # dest2.country = 'United Kingdom'
    # dest2.image = 'country-2.jpg'
    # dest2.cities = 5
    # dest2.price = 1600
    # dest2.offer = True

    # dest3 = Desinations()
    # dest3.country = 'Australia'
    # dest3.image = 'country-4.jpg'
    # dest3.cities = 5
    # dest3.price = 1400

    dests = Desinations.objects.all() #[dest1, dest2, dest3, dest1, dest2, dest3]

    return render(request, 'index.html', {'dests': dests })