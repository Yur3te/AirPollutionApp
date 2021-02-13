import config
import requests
import geocoding
import autolocate

key = config.airlykey

#sprawdzanie czy funkcja autolocate jest włączona, a jeżeli jest to ją stosuje
if autolocate.auto == True:
    lat = autolocate.lat
    lng = autolocate.lng
else:   
    lat = geocoding.lat
    lng = geocoding.lng

#parametry do requestu
params = {'lat': lat,
'lng': lng,
'apikey': key}

#adresy url 
locateurl = 'https://airapi.airly.eu/v2/installations/nearest/'
infourl = f'https://airapi.airly.eu/v2/measurements/point'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}

# print(f'link to instalations: {locateurl}?lat={lat}&lng={lng}&apikey={key}')
# print(f'link to measurements: {infourl}?lat={lat}&lng={lng}&apikey={key}')

#requesty do installations oraz measurements
rinfo = requests.get(infourl, params=params, headers=headers)
rlocate = requests.get(locateurl, params=params, headers=headers)

#definiowanie jsonów 
rinfo_dict = rinfo.json()
rlocate_dict = rlocate.json()

#wyciąganie danych z jsonów
city = rlocate_dict[0]['address']['city']
pollutionLevel = rinfo_dict['current']['indexes'][0]['value']
description = rinfo_dict['current']['indexes'][0]['description']

#dane pm1
pm1 = rinfo_dict['current']['values'][0]['value']

#dane pm25
pm25 = rinfo_dict['current']['values'][1]['value']
pm25Limit = rinfo_dict['current']['standards'][0]['limit']
pm25precent = rinfo_dict['current']['standards'][0]['percent']

#dane pm10
pm10 = rinfo_dict['current']['values'][2]['value']
pm10Limit = rinfo_dict['current']['standards'][1]['limit']
pm10precent = rinfo_dict['current']['standards'][1]['percent']

#inne dane pogodowe
#ciśnienie
pressure = rinfo_dict['current']['values'][3]['value']
#wilgotność
humidity = rinfo_dict['current']['values'][4]['value']
#temperatura
temperature = rinfo_dict['current']['values'][5]['value']


#wypisywanie wszystkich danych
print(f"Stats from {city}")
print(f"Level of air pollution is: {pollutionLevel} CAQI, what means it's {description}")
print("----------------------------")
print("Other air pollutions:")
print(f'Level of pm1 is {pm1}')
print(f'Level of pm25 is {pm25}. Limit of pm25 is {pm25Limit}, what meands current pollution is {pm25precent}%')
print(f'Level of pm10 is {pm10}. Limit of pm10 is {pm10Limit}, what meands current pollution is {pm10precent}%')
print("-----------------------")
print("Other weather statistic:")
print(f'Temperature: {temperature}°C')
print(f'Pressure: {pressure}hPa')
print(f'Humidity: {humidity}%')