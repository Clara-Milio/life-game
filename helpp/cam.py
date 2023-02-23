# ensure you have Python (3  or latest)
# ensure you have pip installer
import requests 
from bs4 import BeautifulSoup 

import csv
import re



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
def getEndpoints(soup):
    #ATTENTION, la suite de cette fonction ne marche que pour mon site, c'est un exemple
    #l'exercice etant de refaire une fonction pour VOTRE site a scraper
    articles = soup.findAll("article")
    # link = theSoupy.findAll("a", {"class":"c-overlay__link"})
    links = []
    # cpt = 0
    for article in articles:
        a = article.find("a", {"class":"c-overlay__link"})
        try:
            links.append(baseUrl + a['href'])
            # cpt+=1
        except:
            pass
        return links

def swoup(url, process):
    #Instanciation de mon proxy
    response = requests.get(url)
    #si mon site renvoie un code HTTP 200 (OK)
    if response.ok:
        #je passe le contenue html de ma page dans un "parser"
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            #Je retourne l'execution de ma fonction process prenan ma SWOUP SWOUP en parametre
            return process(soup)
        except Exception:
            print("ERROR: Impossible to process ! On :" + str(url))
            return False

    else:
        print("ERROR: Failed Connect on :" + str(url))
        return False
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
    print(swoup(link, getEndpoints))
    urls.extend(addBaseUrl(baseUrl, swoup(link, getEndpoints)))
        
print(urls)

# def fileWriter(file,fieldnames, data):
#     with open(file, 'w', encoding='UTF8', newline='') as f:
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(data)

# def tryToCleanOrReturnBlank(str):
#     try:
#         result = str.getText().strip()
#     except:
#         result = ""
#     return result

# def getInfoByPage(soup):
#     fiches = []
#     contacts = soup.find("div",{"class": "coordonnees"})
#     if contacts is not None:
#         tabs = contacts.findAll('li', {"class": "accordeon-item"})
#         if tabs is not None:
#             for contact in tabs:
#                 name = tryToCleanOrReturnBlank(contact.find("div", {"class": "accordeon-header"}))
#                 coord = contact.find("div", {"class": "accordeon-body"})
#                 adress = coord.find("p")
#                 tel = tryToCleanOrReturnBlank(coord.find("a", {"class": "tel"}))
#                 email = tryToCleanOrReturnBlank(coord.find("a", {"class": "email"}))
#                 title = tryToCleanOrReturnBlank(soup.find("title"))
                
#                 try:
#                     adress = adress.getText()
#                     cleanArrAdress = []
#                     for ele in str(adress).split("\n"):
#                         if ele != "":
#                                 cleanArrAdress.append(ele.strip())
                    
#                     realAdress = cleanArrAdress[0]
#                     realCC = cleanArrAdress[1]
#                     realCountry = cleanArrAdress[2]
#                 except:
#                     adress = ""
#                     realAdress =""
#                     realCC =""
#                     realCountry =""
#                     cleanArrAdress = []

#                 fiche = {
#                     "title": title.replace(' - Studyrama', ""),
#                     "name": name,
#                     "adress": " ".join(cleanArrAdress),
#                     "realAdress": realAdress,
#                     "departement": realCC,
#                     "country": realCountry,
#                     "tel": tel,
#                     "email": email
#                 }
#                 fiches.append(fiche)
#     return fiches 


# with open("linkList.csv", 'r', encoding="UTF8", newline='') as file:
#     # reader = csv.DictReader(file, delimiter= '|')

#     reader = csv.DictReader(file)
#     i = 0
#     fiches = []
#     for row in reader:
#         if i < 30:
#         # print(row['link'])
#             fiches.extend(swoup(row['link'], getInfoByPage))
#             i += 1
# print(fiches)


# fieldnamesFiches =  ["title","name","adress", "realAdress", "departement", "country", "tel","email"]
# fileWriter('contacts.csv',fieldnamesFiches, fiches)
# print("Done")



