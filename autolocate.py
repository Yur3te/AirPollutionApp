import requests

auto = False

#system autolocate, który szuka lokalizacji po ip
if auto == True:
    r = requests.get('https://ipinfo.io')
    locate = r.json()['loc']
    lat = locate[0:6]
    lng = locate[8:-1]
    # print(lat,lng)