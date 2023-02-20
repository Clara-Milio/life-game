# ensure you have Python (3  or latest)
# ensure you have pip installer
import requests 
from bs4 import BeautifulSoup 
import csv

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
    articles = theSoupy.findAll("article")
    # link = theSoupy.findAll("a", {"class":"c-overlay__link"})
    links = []
    cpt = 0
    for article in articles:
        a = article.find("a", {"class":"c-overlay__link"})
        try:
            links.append(baseUrl + a['href'])
            cpt+=1
        except:
            pass
#     # divs = theSoupy.find('div', {"class": "o-grid"})
#     # # for div in divs: 
#     # didiv = divs.findAll('span')
#     # links = []
#     ul = theSoupy.find("ul", {"class":"o-grid--1@sm"})
#     for diva in didiv:
#         a = diva.find('a')
#         try:
#             links.append(a['href'])
#                 # print(baseUrl + a['href'])
#                 # requests.get(baseUrl + a['href'])
#         except:
#             pass
#             # print(diva)
#             # print('ERROR: No link')
#             return links

def sousoup(url, process):
    #Instanciation de mon proxy
    response = requests.get(url)
    #si mon site renvoie un code HTTP 200 (OK)
    if response.ok:
        #je passe le contenue html de ma page dans un "parser"
        theSoupy = BeautifulSoup(response.text, 'html.parser')
        try:
            #Je retourne l'execution de ma fonction process qui prend ma SWOUP  en parametre
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


# def getInfoPage(theSoupy):
    # fiches = []
    # contact = theSoupy.find("div", {"class":"coordonnees"})
    # if contact is not None:
    #     tabs = contact.findAll("li", {"class": "accordeon-item"})
        # if tabs is not None:
        #     for tab in tabs:
                # print(tab)
                # name = tab.find("div",{"class":"accordeon-header"})
                # print(name.getText())
                # coord = tab.find("div", "class": "accordeon-body")
                # address = coord.find("p")
                # fichenkdlk,dk,fd
                # fiches.append(fiche)
                # return fiches
# exit()

#     print(contacts)


#Execution
urls = []
for link in getLinks(baseUrl + uri, 4):
    print("Checking " + link)
    urls.extend(addBaseUrl(baseUrl, sousoup(link, crawlEndPoint)))
print(urls)


# with open('personnes.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader: 
#         print(row['email'])

headers = ["id", "category", "link"]
rows = []

for i in range(200):
    rows.append({
        "id": i,
        "category": "Generated",
        "link": "https://www.google.com"
    })

# fieldnames = ['id', 'category', 'link']
with open('linkList.csv', 'w',  encoding="UTF8", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

# with open('linkList.csv', 'r', encoding="UTF8", newline='') as file:
#     reader = csv.DictReader(file, fieldnames=headers)
    # fiches = []
#     for line in reader:
#         print(line['link'])
#         sousoup(line["link"], getInfoPage)

print("Done")