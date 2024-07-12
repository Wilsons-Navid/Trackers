import requests

# using the ipify.org to collect my public Ip_address
ip_address = requests.get("http://api.ipify.org").text
print(ip_address)
# another Rest AOI request to get more information
response = requests.get(f"http://ip-api.com/json/{ip_address}").json()
print(response)

print(response['city'])

# redirecting to a map

city = response['city']

# Generate a Google Maps link using the city
map_link = f"https://www.google.com/maps/search/?api=1&query={city}"

# print the link

print(map_link)