from urllib.request import urlopen, URLError
from bs4 import BeautifulSoup as bs
import re


pages = set()

def getLinks(pageUrl):
    global pages
    try:
        html = urlopen('https://en.wikipedia.org' + pageUrl)
    except URLError as error:
        print(error)
        return None
    try:
        bsObj = bs(html, 'lxml')
        print(bsObj.h1.get_text())
        text = bsObj.find(id='mw-content-text').find_all('p')
        if len(text) > 0:
            print(text[0].get_text())
        else:
            print('\n************** Text is None ***************\n')
        edit = bsObj.find(id='ca-edit')
        if edit != None:
            print(edit.find('span').find('a').attrs['href'])
        else:
            print('************** Edit is None *************')
        links = bsObj.find_all('a', href=re.compile('^(/wiki/)'))
    except AttributeError as error:
        print(error)
    else:
        for link in links:
            if 'href' in link.attrs:
                if link.attrs['href'] not in pages:
                    newPage = link.attrs['href']
                    print('------------------------\n' + newPage)
                    pages.add(newPage)
                    getLinks(newPage)

getLinks('')
