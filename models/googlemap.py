import requests

def getLatLong(search_token):
    url='https://maps.googleapis.com/maps/api/geocode/json'
    mysensor = 'false'
    api_key = 'API KEY GOES HERE'
    payload = {'address':search_token, 'sensor':mysensor, 'key': api_key}
    r = requests.get(url, params=payload)

    json = r.json()
    
    lat = json['results'][0]['geometry']['location']['lat'] if len(json['results']) != 0 else None
    lon = json['results'][0]['geometry']['location']['lng'] if len(json['results']) != 0 else None

    return lat, lon





