import requests, sys, os, time, json
from bs4 import BeautifulSoup
from time import gmtime, strftime

if os.path.exists('log.txt'):
    f = open('log.txt', 'r')
else:
    f = open('log.txt', 'w')
    f.close()
    f = open('log.txt', 'r')

tm = time.strftime("%Y-%m-%dT%H:%M:%S.067Z", gmtime())

url = "https://www.epicgames.com/graphql?operationName=searchStoreQuery&variables=%7B%22allowCountries%22:%22RU%22,\
%22category%22:%22games%2Fedition%2Fbase%7Csoftware%2Fedition%2Fbase%7Ceditors%7Cbundles%2Fgames%22,%22count%22:1000,\
%22country%22:%22RU%22,%22effectiveDate%22:%22[," + tm + "]%22,%22keywords%22:%22%22,%22locale%22:%22ru%22,\
%22onSale%22:true,%22releaseDate%22:%22[," + tm + "]%22,%22sortBy%22:%22releaseDate%22,%22sortDir%22:%22DESC%22,%22start%22:0,%22tag%22:%22%22,\
%22withPrice%22:true%7D&extensions=%7B%22persistedQuery%22:%7B%22version%22:1,%22sha256Hash%22:%226e7c4dd0177150eb9a47d624be221929582df8648e7ec271c821838ff4ee148e%22%7D%7D"
headers = {
    "accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    }
req = requests.get(url, headers=headers)

for item in json.loads(req.text)['data']['Catalog']['searchStore']['elements']:
    if item['price']['totalPrice']['fmtPrice']['intermediatePrice'] == '0':
        t = 'true'
        for line in f:
            if line.replace('\n', '') == item['title']:
                t = 'false'
        if t == 'true':
            f.close()
            f = open('log.txt', 'a')
            f.write('\n' + item['title'])
            f.close()
            f = open('log.txt', 'r')
            print('Скидка 100% на игру ' + item['title'])
            requests.get('https://api.telegram.org/botXXXXXXXXXXXXXXXXXXXXXXXXXX/sendMessage?chat_id=XXXXXXXXXXXXX&text=' \
            + 'Скидка 100% на игру ' + item['title'] + '\n\nhttps://www.epicgames.com/store/ru/p/' + item['catalogNs']['mappings'][0]['pageSlug']);
f.close()

print("\nEnd program")
