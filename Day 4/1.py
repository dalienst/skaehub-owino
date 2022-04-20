#find details of a given zip code

from geopy.geocoders import Nominatim

def get_address(zipcode):
    locator = Nominatim(user_agent="geoapiExercises")
    location = locator.geocode(zipcode)
    address = location.address
    return address

print(get_address(80101))