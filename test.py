# ensure you have Python (3  or latest)
# ensure you have pip installer
import requests 
from bs4 import BeautifulSoup 
import csv

# L'url du site que je souhaite Scraper
baseUrl = 'https://www.orpi.com'
uri = "/recherche/rent?transaction=rent&page="
response = requests.get(baseUrl)


print(response)
theSoupy = BeautifulSoup(response.text, 'html.parser')
articles = theSoupy.findAll("article")
link = theSoupy.findAll("a", {"class":"c-overlay__link"})
#print(link)

links = []
cpt = 0
for article in articles:
    a = article.find("a", {"class":"c-overlay__link"})
    try:
        links.append(baseUrl + a['href'])
        cpt+=1
    except:
        pass
print('SKDQLJDZAIDIHDQDSQ\n:',links)
print(cpt)
