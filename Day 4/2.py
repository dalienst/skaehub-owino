#calculate distance from Cairo to Nairobi

from geopy.geocoders import Nominatim
from geopy import distance

first_city = 'Cairo'
second_city = 'Nairobi'

def get_distance_between_city(first_city, second_city):
    locater = Nominatim(user_agent="geoapiExercises")
    l1 = locater.geocode(first_city)
    l2 = locater.geocode(second_city)
    location_one = ((l1.latitude, l1.longitude))
    location_two = ((l2.latitude, l2.longitude))
    distance_cairo_and_nairobi = distance.distance(location_one, location_two).km, "kilometres"
    return distance_cairo_and_nairobi

print(get_distance_between_city(first_city, second_city))