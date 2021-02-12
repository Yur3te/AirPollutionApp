import config
import requests

key = config.geocodingkey

address = "Kozy"

params = {
    'key': key,
    'q': address
}

url = f'https://api.opencagedata.com/geocode/v1/json?'
r = requests.get(url, params=params)
rlocalisation_dict = r.json()

lat = rlocalisation_dict['results'][0]['geometry']['lat']
lng = rlocalisation_dict['results'][0]['geometry']['lng']
# print(lat, lng)