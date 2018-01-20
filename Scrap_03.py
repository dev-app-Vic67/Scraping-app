from urllib.request import urlopen, URLError
from bs4 import BeautifulSoup
import re


def getBSObj(url):
    try:
        html = urlopen(url)
        bsObj = BeautifulSoup(html, 'lxml')
    except URLError as error:
        print(error)
        return None
    else:
        return bsObj


def printChildren(bsObj):
    try:
        children = bsObj.find("table",{"id":"giftList"}).children
    except AttributeError as error:
        print(error)
    else:
        for child in children:
            print(child)


def printSibling(bsObj):
    try:
        siblings = bsObj.find("table",{"id":"giftList"}).tr.next_siblings
    except AttributeError as error:
        print(error)
    else:
        for sibling in siblings:
          print(sibling)


def printParent(bsObj):
    try:
        price = bsObj.find('img', {'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text()
    except AttributeError as error:
        print(error)
    else:
        print(price)
        print(bsObj.img.attrs['src'], '\n')

def printImagesPath(bsObj):
    try:
        regex = re.compile(r'^../img/gifts/img.*.jpg$')
        images = bsObj.find_all('img', {'src': regex})
        for image in images:
            print(image['src'])
    except AttributeError as error:
        print(error)


url = 'http://www.pythonscraping.com/pages/page3.html'

bsObj = getBSObj(url)

if bsObj != None:
    print("\n01 -------------------------------")
    printChildren(bsObj)
    print("02 -------------------------------")
    printSibling(bsObj)
    print("03 -------------------------------")
    printParent(bsObj)
    print("04 -------------------------------\n")
    printImagesPath(bsObj)
else:
    print("Soup not ready!")
