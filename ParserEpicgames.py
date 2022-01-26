import requests, sys, os
from bs4 import BeautifulSoup

#f = open('log', '+')
if os.path.exists('log.txt'):
    f = open('log.txt', 'r')
else:
    f = open('log.txt', 'w')
    f.close()
    f = open('log.txt', 'r')

url = "https://www.epicgames.com/store/ru/browse?sortBy=releaseDate&sortDir=DESC&priceTier=tierDiscouted&count=100&start=0"
headers = {
    "accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    }
req = requests.get(url, headers=headers)
src = req.text
soup = BeautifulSoup(src, "lxml")
#print(soup)
obj = soup.findAll("div", {"class": "css-hkjq8i"})
#print(obj)
c = 0
w = ''
t = 'true'
for i in obj:
    x = ''
    c = c + 1
    if c > len(obj) / 3:
        print("Program exit")
        sys.exit()
    if i.find("div", {"class": "css-b0xoos"}).text == "-100 %":
        x = i.find("div", {"data-testid": "direction-auto"}).text
        t = 'true'
        for line in f:
            if line == x :
                t = 'false'
                break
        if t:
            f.close()
            f = open('log.txt', 'a')
            f.write('\n' + x)
            f.close()
            f = open('log.txt', 'r')
            x = x + " (Скидка " + i.find("div", {"class": "css-b0xoos"}).text + ")"
            print(x)
f.close()
print("End program")



#https://www.epicgames.com/store/ru/browse?sortBy=releaseDate&sortDir=DESC&priceTier=tierDiscouted&count=40&start=0