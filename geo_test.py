import requests, json

url = 'http://photon.komoot.de/api/?q='
addresses = ['Гагарина 36 Сочи', ]

for address in addresses:
    resp = requests.get(url=url+address)
    data = json.loads(resp.text)
    print(data['features'][0]['geometry'])
    print(data['features'][0]['geometry']['coordinates'][0])
    print(data['features'][0]['geometry']['coordinates'][1])