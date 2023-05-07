import googlemaps
import pprint
import time

# Define client w/ API key
gmaps = googlemaps.Client(key='AIzaSyAD55_uoXChGGyrm0RIK4rubxopML48oO4')

# Define user location (not sure how to get this)
userLocation = '43.650756, -79.391594' #latitude and longitude

# Define search
places_result = gmaps.places_nearby(location= userLocation, radius = 40000, open_now = False, type = 'hospital')

pprint.pprint(places_result)
