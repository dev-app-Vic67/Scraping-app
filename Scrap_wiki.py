from urllib.request import urlopen, URLError
from bs4 import BeautifulSoup
import datetime
import random
import re


random.seed(datetime.datetime.now())

def getLinks(url):

    try:
        html = urlopen('https://en.wikipedia.org' + url)
    except URLError as error:
        print(error)
        return None
    try:
        bsObj = BeautifulSoup(html, 'lxml')
        links = bsObj.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    except AttributeError as error:
        print(error)
        return None
    else:
        return links


url = '/wiki/Kevin_Bacon'

links = getLinks(url)

if links != None:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)

