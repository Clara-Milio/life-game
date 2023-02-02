# ensure you have python and pip installer
import requests
from bs4 import BeautifulSoup

# Url to scrap
baseUrl = 'https://www.orpi.com'
endUrl = '/recherche/rent?transaction=rent&resultUrl=&realEstateTypes%5B0%5D=maison&realEstateTypes%5B1%5D=appartement&agency=&minSurface=&maxSurface=&minLotSurface=&maxLotSurface=&minStoryLocation=&maxStoryLocation=&newBuild=&oldBuild=&minPrice=&maxPrice=&sort=date-down&layoutType=mixte&page=&recentlySold=false'

# proxy 
#Il ne faut pas mettre d'espace ici
response = requests.get(baseUrl + endUrl)

# Let's crawl on the website ! (take all the links)
def crawl(theSoupy): 
    #il n'y a rien dans la div que tu vise (apres j'ai testé avec mon lien hein.. )
    #Mais au moins tu rentre dans ta fonction sans erreurs
    div = theSoupy.find('div', {"class": "c-box__inner c-box__inner--sm c-overlay"})
    print(div)
    spans = div.findAll('span')
    for span in spans:
        a = span.find('a')
        try:
            print(baseUrl + a['href'])
            requests.get(baseUrl + a['href'])
        except:
            pass

# parser
if response.ok:
    soupySoup = BeautifulSoup(response.text,'html.parser')

    #Tu as oublié d'appeler la fonction crawl :
    crawl(soupySoup)