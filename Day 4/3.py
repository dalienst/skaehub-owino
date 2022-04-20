# get country, state, city of a given latitude and longitude

from geopy.geocoders import Nominatim

def get_city_state_country(lat, long):
    locater = Nominatim(user_agent="geoapiExercises")
    location = locater.reverse((lat, long), exactly_one=True)

    address = location.raw['address']
    city = address['city']
    state = address['state']
    country = address['country']

    return city, state, country
