import requests
import json
import pprint
r = requests.get('http://www.geoplugin.net/json.gp')
accuweatherAPIKey = '75QyRANkAUFCJMjsfSF6wiE1zDU1j9QD'

if (r.status_code != 200):
    print('Não foi possível obter a localização')
else:
    localizacao = json.loads(r.text)
    longi = localizacao['geoplugin_longitude']
    lat = localizacao['geoplugin_latitude'] 
    print( pprint.pprint( localizacao ))
    print('lat: ', lat)
    print('long: ', longi)

    LocationAPIUrl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?"\
    +"apikey="+accuweatherAPIKey+"&q="+lat+"%2C"+longi+"&language=pt-br"

    r2 = requests.get(LocationAPIUrl)
    if(r.status_code != 200):
        print("Não foi possível obter o código do local")
    else:
        print(pprint.pprint(json.loads(r2.text)))


