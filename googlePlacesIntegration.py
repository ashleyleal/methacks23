import googlemaps
from datetime import datetime, timedelta
from key import Key

# Define client w/ API key
gmaps = googlemaps.Client(key= Key)

# Clear file
open("locations.txt", "w").close()

# Define user location (not sure how to get this)
userLocation = '43.650756, -79.391594' #latitude and longitude

places_result = gmaps.places_nearby(location=userLocation, radius=40000, open_now=False, type='hospital')

for place in places_result['results'][:10]:
    name = place['name']
    address = place['vicinity']
    place_id = place['place_id']

    place_details = gmaps.place(place_id=place_id, fields=['opening_hours'])
    if 'opening_hours' in place_details['result']:
        opening_hours = place_details['result']['opening_hours']['weekday_text']
    else:
        opening_hours = "Not available"
        
    output = f"Name: {name}\nAddress: {address}\nOpening Hours: {opening_hours}\n"

    f = open("locations.txt", "a")
    f.write(output)
    print(output)
