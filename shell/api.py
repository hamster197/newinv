import requests

url = "https://ads-api.ru/main/api?user=insochi@century21.ru&token=c4eef57751055fc4fc9e376e9448d06d&price1=6500000&price2=6500000&city=Сочи&phone=89881459041&category_id=2"
       #https://ads-api.ru/main/api?user=insochi@century21.ru&token=c4eef57751055fc4fc9e376e9448d06d&price1=6500000&price2=6500000&city=Сочи&phone=89881459041&category_id=2
payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
urls = []
jmain= dict(response.json())
for i in jmain['data']:
    urls.append(i['url'])

for i in urls:
    print(i)