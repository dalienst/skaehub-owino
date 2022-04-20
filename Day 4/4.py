#search a country from a given state

from geopy.geocoders import Nominatim

def country_name(state):
    geolocator = Nominatim(user_agent='geoapiExercises')
    location = geolocator.geocode(state)
    country_name = location.address
    return country_name

print(country_name('Kitui'))