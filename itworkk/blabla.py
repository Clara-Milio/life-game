# ensure you have Python (3  or latest)
# ensure you have pip installer
import requests 
from bs4 import BeautifulSoup 
import csv

# L'url du site que je souhaite Scraper
baseUrl = 'https://www.orpi.com'
uri = "/recherche/rent?transaction=rent&page="
response = requests.get(baseUrl)
urls = []
links = []

headers = ["id", "category", "link"]
rows = []

def getElements(baseUrl, theSoupy):
    articles = theSoupy.findAll("article")
    link = theSoupy.findAll("a", {"class":"c-overlay__link"})

    cpt = 0

    print("\n\nChecking : " + baseUrl)
    for article in articles:
        a = article.find("a", {"class":"c-overlay__link"})
        try:
            links.append(baseUrl + a['href'])
            cpt+=1
        except:
            pass
    
    for link in links:
        print(link)

def getLinks(url, nbPg):
    for i in range(nbPg):
        urls.append(url + str(i))
    return urls

def getInfoByPage(theSoupy):
    fiches = []
    informations = theSoupy.find("article", {"class":"c-box--highlighted"})
    if informations is not None:
        capsule = informations.find('span', {"class": "u-text-md"})
        if capsule is not None:
            typeBien = capsule.find("a", {"class": "u-link-unstyled"}).getText()
            price = informations.find("strong", {"class": "u-text-md"}).getText()
            city = informations.find("p", {"class": "u-mt-sm"}).getText()

            fiche = {
                "typeBien": typeBien,
                "price" : price,
                "city" : city
            }
            fiches.append(fiche)
    return fiches 

# PLAN
theSoupy = BeautifulSoup(response.text, 'html.parser')
getElements(baseUrl, theSoupy)
getLinks(baseUrl + uri, 4)
for url in urls:
    getElements(url, theSoupy)

# Create Link list
i = 0
for link in links:
    rows.append({
        "id": i,
        "category": "Generated",
        "link": str(link)
    })
    i += 1
with open('linkList.csv', 'w',  encoding="UTF8", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

# Create Infos list
getInfoByPage(theSoupy)

def fileWriter(file,fieldnames, data):
    with open(file, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


with open("linkList.csv", 'r', encoding="UTF8", newline='') as file:
    # reader = csv.DictReader(file, delimiter= '|')

    reader = csv.DictReader(file)
    i = 0
    fiches = []
    for row in reader:
        if i < 30:
        # print(row['link'])
            fiches.extend(theSoupy(row['link'], getInfoByPage))
            i += 1
print(fiches)


fieldnamesFiches =  ["typeBien", "price", "city"]
fileWriter('infoByPage.csv',fieldnamesFiches, fiches)
print("Done")

        

# def fileWriter(infoByPage.csv,fieldnamesFiches, fiches):
#     with open(file, 'w', encoding='UTF8', newline='') as f:
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(data)

# with open("linkList.csv", 'r', encoding="UTF8", newline='') as file:
#     # reader = csv.DictReader(file, delimiter= '|')
#     reader = csv.DictReader(file)
#     i = 0
#     fiches = []
#     for row in reader:
#         if i < 30:
#         # print(row['link'])
#             fiches.extend(theSoupy(row['link'], getInfoByPage))
#             i += 1
# print(fiches)
# fieldnamesFiches =  ["title","name","adress", "realAdress", "departement", "country", "tel","email"]
# fileWriter('infoByPage.csv',fieldnamesFiches, fiches)
