# ensure you have python and pip installer
import requests
from bs4 import BeautifulSoup

# Url to scrap
baseUrl = 'https://www.orpi.com'
endUrl = '/recherche/rent/'

# proxy
response = requests.get (baseUrl + endUrl)

# Let's crawl on the website ! (take all the links)
def crawl(theSoupy): 
    div = theSoupy.find('div', {"class": "c-box__inner c-box__inner--sm c-overlay"})
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