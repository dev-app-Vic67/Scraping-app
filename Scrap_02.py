from urllib.request import urlopen, URLError
from bs4 import BeautifulSoup, NavigableString


http = 'http://www.pythonscraping.com/pages/warandpeace.html'

try:
    html = urlopen(http)
except URLError as error:
    print(error)
try:
    bsObj = BeautifulSoup(html, 'lxml')
    nameList = bsObj.findAll('span', {'class':'green'})
except AttributeError as error:
    print(error)
else:
    for name in nameList:
        print(name.get_text())
