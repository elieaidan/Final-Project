from django.shortcuts import render, redirect
from random import choice
from .models import City, Activity, Hotel
from django.db.models import Q
from django.contrib import messages

def search(request):
    cities = City.objects.all()
    return render(request, 'search.html', {'cities': cities})


def search_result(request):
    if request.method == 'POST':
        city_name = request.POST.get('city')
        price = request.POST.get('price')
        

        if not city_name and not price:
            messages.error(request, 'Veuillez sélectionner une ville et entrer un prix.')
            return redirect('search')
        elif not city_name:
            messages.error(request, 'Veuillez sélectionner une ville.')
            return redirect('search')
        elif not price:
            messages.error(request, 'Veuillez entrer un prix.')
            return redirect('search')

        city = City.objects.get(name=city_name)
        activities = Activity.objects.filter(city=city, price__lte=price).order_by('price')
        return render(request, 'search_result.html', {'activities': activities, 'city': city, 'price': price })
    else:
        return redirect('search')


    
def accueil(request):
    return render(request, 'acceuil.html')

def hotel_search(request):
    if request.method == 'POST':
        city_name = request.POST.get('city')
        price_per_night = request.POST.get('price_per_night')

        if not city_name and not price_per_night:
            messages.error(request, 'Veuillez sélectionner une ville et entrer un prix par nuit.')
            return redirect('hotel_search')
        elif not city_name:
            messages.error(request, 'Veuillez sélectionner une ville.')
            return redirect('hotel_search')
        elif not price_per_night:
            messages.error(request, 'Veuillez entrer un prix par nuit.')
            return redirect('hotel_search')

        try:
            price_per_night = float(price_per_night)
        except ValueError:
            messages.error(request, 'Le prix doit être un nombre décimal.')
            return redirect('hotel_search')

        city = City.objects.get(name=city_name)
        hotels = Hotel.objects.filter(city=city, prix_per_night__lte=price_per_night).order_by('prix_per_night')
        return render(request, 'hotel_search_results.html', {'hotels': hotels, 'city': city, 'price_per_night': price_per_night})
    else:
        cities = City.objects.all()
        return render(request, 'hotel_search.html', {'cities': cities})
    
def hotel_search_results(request):
    city = request.GET.get('city')
    max_price = request.GET.get('max_price')

    if city and max_price:
        try:
            max_price = float(max_price)
        except ValueError:
            messages.error(request, 'Le prix maximum doit être un nombre décimal.')
            return redirect('hotel_search')

        hotels = Hotel.objects.filter(city__name__icontains=city, prix_per_night__lte=max_price).order_by('prix_per_night')

        hotel_list = []
        for hotel in hotels:
            hotel_dict = {
                'name': hotel.name,
                'address': hotel.address,
                'city': hotel.city,
                'prix_per_night': hotel.prix_per_night,
                'nombre_etoiles': hotel.nombre_etoiles,
                'url': hotel.url
            }
            hotel_list.append(hotel_dict)

        return render(request, 'hotel_search_results.html', {'hotels': hotel_list})
    else:
        return render(request, 'hotel_search.html')



def random_destination(request):
    cities = City.objects.all()
    random_city = choice(cities)
    message = f"{random_city.name}"
    context = {'message': message}
    return render(request, 'random_destination.html', context)
