import requests, json

from crm.models import flat_obj

url = 'http://photon.komoot.de/api/?q='
addresses = ['Гагарина 36 Сочи', ]

#for address in addresses:
for subj in flat_obj.objects.all():
    adres = subj.adress + ' '
    if subj.type != 'uchastok':
        adres = adres + subj.dom_numb + ' '
    else:
        adres = adres + subj.uc_dom_nunb + ' '
    if len(subj.kr_raion) == 0:
        adres = adres + 'Сочи'
    else:
        adres = adres + 'Краснодар'
    resp = requests.get(url=url + adres)
    data = json.loads(resp.text)
    # addresses = ['Гагарина 36 Сочи', ]
    subj.latitude = data['features'][0]['geometry']['coordinates'][0]
    subj.longitude = data['features'][0]['geometry']['coordinates'][1]
    subj.save()
    # resp = requests.get(url=url+address)
    # data = json.loads(resp.text)
    # print(data['features'][0]['geometry'])
    # print( data['features'][0]['geometry']['coordinates'][0])#'latitude='
    # print(data['features'][0]['geometry']['coordinates'][1])#'longitude='