# Note: I learned this from Geeks4Geeks. The link is provided here: https://www.geeksforgeeks.org/how-to-get-geolocation-in-python/

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="ak_geocoder")
location = input("Enter your current location: ")

def get_coordinates(place):
    location = geolocator.geocode(place)
    if location:
        return location.latitude, location.longitude
    return "Location not found"

coordinates = list(get_coordinates(location))
print(coordinates)
