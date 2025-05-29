from geopy.geocoders import Nominatim
from pyowm import OWM
from pyowm.utils import geo
print("DISCLAIMER: The UV index is of the highest UV in a day based off your location.")
owm = OWM('0d469ea5fc54bc0eb446a53889fd5c3f')
mgr = owm.uvindex_manager()

geolocator = Nominatim(user_agent="ak_geocoder")

def get_coordinates(place):
    location = geolocator.geocode(place)
    if location:
        return location.latitude, location.longitude
    return "Location Not Found"

def get_uv_index():
    global lat, lon
    uni = mgr.uvindex_around_coords(lat, lon)
    return uni.value

def match_uv(uv_amount):
    # For reference
    uvamount_recommendedSPF = {"0-2":15,
                           "3-5":30,
                           "6-7":40,
                           "8-10":50,
                           "11+":"Stay indoors"}
    
    if uv_amount <= 2:
        print("Apply 15 SPF for general protection")
    elif uv_amount >= 3 and uv_amount <= 5:
        print("SPF 30 or higher is recommended")
    elif uv_amount >= 6 and uv_amount <= 7:
        print("SPF 30-40 is recommended, and it's best to seek shade and limit sun exposure during the afternoon")
    elif uv_amount >= 8 and uv_amount <= 10:
        print("SPF 50+ is recommended, along with wearing protective clothing, sunglasses, and seeking shade")
    elif uv_amount >= 11:
        print("SPF 50-60 9s highly recommended. Try to stay indoors during peak hours")
    else:
        print("Location not supported") # If location data is not on API, print this to user

while True:
    location = input("Enter your current location: ")
    if get_coordinates(location) != "Location Not Found":
        coordinates = list(get_coordinates(location))
        lat = coordinates[0]
        lon = coordinates[1]
        uv = get_uv_index()
        match_uv(uv)
        print()
    else:
        print("Location not found. Exiting application")
        break
