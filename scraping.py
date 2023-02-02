# ensure you have python and pip installer
import requests
from bs4 import BeautifulSoup

# Url to scrap
baseUrl = 'https://www.orpi.com'
endUrl = '/recherche/rent/'

# proxy 
#Il ne faut pas mettre d'espace ici
response = requests.get(baseUrl + endUrl)

# Let's crawl on the website ! (take all the links)
def crawl(theSoupy): 
    #il n'y a rien dans la div que tu vise
    #au moins tu rentre dans ta fonction sans erreurs
    div = theSoupy.find('div', {"class": "c-box__inner c-box__inner--sm c-overlay"})
    print(div)
    #retire le pass apres que tu ai réparé ça :) 
    pass
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