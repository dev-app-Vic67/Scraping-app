from urllib.request import urlopen, URLError
from bs4 import BeautifulSoup


def getTitle(url):
    """Read titles from the html-page"""
    try:
        html = urlopen(http)                       # save http-page to html
    except URLError as error:
        print(error)
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'lxml') # parsing html
        title = bsObj.h1                           # get tag object
    except AttributeError as error:
        print(error)
        return None
    return title


http = 'http://pythonscraping.com/pages/page1.html'

title = getTitle(http)
if title == None:
    print("Title not found")
else:
    print(title)

