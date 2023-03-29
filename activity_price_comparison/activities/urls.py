from django.urls import path
from .views import search, search_result, hotel_search, accueil, hotel_search_results,random_destination

urlpatterns = [
    path('', accueil, name='accueil'),
    path('search/', search, name='search'),
    path('result/', search_result, name='search_result'),
    path('hotel/', hotel_search , name='hotel_search'),
    path('hotel_result/', hotel_search_results , name='hotel_search_results'),
    path('random_destination/', random_destination , name='random_destination'),

]
