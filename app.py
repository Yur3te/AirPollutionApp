import config
import requests
import geocoding
import autolocate

key = config.airlykey


if autolocate.auto == True:
    lat = autolocate.lat
    lng = autolocate.lng
else:   
    lat = geocoding.lat
    lng = geocoding.lng


params = {'lat': lat,
'lng': lng,
'apikey': key}


locateurl = 'https://airapi.airly.eu/v2/installations/nearest/'
infourl = f'https://airapi.airly.eu/v2/measurements/point'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}

print(f'link to instalations: {locateurl}?lat={lat}&lng={lng}&apikey={key}')
print(f'link to measurements: {infourl}?lat={lat}&lng={lng}&apikey={key}')

rinfo = requests.get(infourl, params=params, headers=headers)
rlocate = requests.get(locateurl, params=params, headers=headers)

rinfo_dict = rinfo.json()
rlocate_dict = rlocate.json()


city = (rlocate_dict[0]['address']['city'])
pollutionLevel = (rinfo_dict['current']['indexes'][0]['value'])
description = (rinfo_dict['current']['indexes'][0]['description'])



print(f"Stats from {city}")
print(f"Level of air pollution is: {pollutionLevel} CAQI, what means it's {description}")