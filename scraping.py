# ensure you have python and pip installer
import requests
from bs4 import BeautifulSoup

# Url to scrap
baseUrl = 'https://www.orpi.com'
endUrl = '?transaction=rent&resultUrl=&realEstateTypes%5B0%5D=maison&realEstateTypes%5B1%5D=appartement&locations%5B0%5D%5Bvalue%5D=lyon-7&locations%5B0%5D%5Blabel%5D=Lyon%207%20%2869007%29&agency=&minSurface=&maxSurface=&minLotSurface=&maxLotSurface=&minStoryLocation=&maxStoryLocation=&newBuild=&oldBuild=&minPrice=&maxPrice=&sort=date-down&layoutType=mixte&page=&recentlySold=false'

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