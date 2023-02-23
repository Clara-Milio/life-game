# ensure you have Python (3  or latest)
# ensure you have pip installer
import requests 
from bs4 import BeautifulSoup 
# L'url du site que je souhaite Scraper
baseUrl = 'https://www.orpi.com'
uri = "/recherche/rent?transaction=rent&page="


#Genere des liens avec l'argument "page" qui s'incrémente
def getLinks(url, nbPg):
    # initialisation du resultat (vide pour l'instant)
    urls = []
    # Pour chaque page
    for i in range(nbPg):
        # Ajoutes la concatenation de l'url avec l'index au tableau d'urls
        urls.append(url + str(i))
    return urls


#fonction qui permet de "crawler" sur mon site et recuperer tous les liens sur la page visée
def crawlEndPoint(theSoupy): 
    divs = theSoupy.find('div', {"class": "o-grid"})
    # for div in divs: 
    didiv = divs.findAll('span')
    links = []
    for diva in didiv:
        a = diva.find('a')
        try:
            links.append(a['href'])
                # print(baseUrl + a['href'])
                # requests.get(baseUrl + a['href'])
        except:
            pass
            # print(diva)
            # print('ERROR: No link')
            return links

def sousoup(url, process):
    #Instanciation de mon proxy
    response = requests.get(url)
    #si mon site renvoie un code HTTP 200 (OK)
    if response.ok:
        #je passe le contenue html de ma page dans un "parser"
        theSoupy = BeautifulSoup(response.text, 'html.parser')
        try:
            #Je retourne l'execution de ma fonction process prenan ma SWOUP SWOUP en parametre
            return process(theSoupy)
        except Exception:
            print("ERROR: Impossible to process ! " )
    else:
        print("ERROR: Failed Connect")
    return 

#concatene mes liens a l'url
def addBaseUrl(baseUrl, urls):
    res = []
    for url in urls:
        res.append(baseUrl + url)
    return res


#Execution
urls = []
for link in getLinks(baseUrl + uri, 4):
    print("Checking " + link)
    urls.extend(addBaseUrl(baseUrl, sousoup(link, crawlEndPoint)))
        
print(urls)
