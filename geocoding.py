import config
import requests

key = config.geocodingkey

address = "Bielsko-Biała"

params = {
    'key': key,
    'q': address
}

#request do jakiegoś api do geocodingu
url = f'https://api.opencagedata.com/geocode/v1/json?'
r = requests.get(url, params=params)
rlocalisation_dict = r.json()

lat = rlocalisation_dict['results'][0]['geometry']['lat']
lng = rlocalisation_dict['results'][0]['geometry']['lng']