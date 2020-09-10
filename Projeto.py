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
    #print( pprint.pprint( localizacao ))
    #print('lat: ', lat)
    #print('long: ', longi)

    LocationAPIUrl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?"\
    +"apikey="+accuweatherAPIKey+"&q="+lat+"%2C"+longi+"&language=pt-br"

    r2 = requests.get(LocationAPIUrl)
    if(r.status_code != 200): 
        print("Não foi possível obter o código do local")
    else:
        locationResponse = json.loads(r2.text)
        #print(pprint.pprint(json.loads(r2.text)))
        nomelocal = locationResponse ['LocalizedName'] + ", "\
            +locationResponse ['AdministrativeArea']['LocalizedName'] + ". " \
            +locationResponse ['Country']['LocalizedName']
        codigoLocal = locationResponse ['Key']
        print("Obtendo clima do local: ", nomelocal)

        CurrentConditionsAPIUrl = "http://dataservice.accuweather.com/currentconditions/v1/"\
            +codigoLocal+"?apikey="+accuweatherAPIKey+"&language=pt-br"

        r3 = requests.get(CurrentConditionsAPIUrl)
        if(r3.status_code != 200):
            prinnt('Não foi possível obter o código do local')
        else:
            CurrentConditionResponse = json.loads(r3.text)
            textoClima = CurrentConditionResponse[0]['WeatherText']
            temperatura = CurrentConditionResponse[0]['Temperature']['Metric']['Value']
            print('Clima no momento: '+ textoClima)
            print('Temperatura: '+ str(temperatura) + '°')

        



