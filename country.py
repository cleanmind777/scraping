import time
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="your_app_name")

def city_state_country(coord):
    try:
        location = geolocator.reverse(coord, exactly_one=True)
        address = location.raw['address']
        city = address.get('city', '')
        state = address.get('state', '')
        country = address.get('country', '')
        return city, state, country
    except Exception as e:
        print(f"Error geocoding {coord}: {e}")
        return '', '', ''

# Example usage with rate limiting
coords = ["24.471595764160156,54.60591506958008", "34.052235, -118.243683"]

for coord in coords:
    result = city_state_country(coord)
    print(result[2])
    time.sleep(1)  # Sleep for 1 second between requests