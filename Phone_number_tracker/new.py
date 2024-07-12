import phonenumbers
from phonenumbers import geocoder
from test import number
import folium
key = "36bf3288a299471a9dad534e6b836424"
#Finding country of  phonenumber 
check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")
print(number_location)

# finding the service provider
from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

#Using maps to point out the location using the opencage module

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)

query = str(number_location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
# Print the latitude and longitude
print(lat, lng)

# using folium to redirect to a map

map_location = folium.Map(location= [lat, lng], zoom_start=9)
folium.Marker([lat,lng], popup=number_location).add_to(map_location)

map_location.save("mylocation.html")