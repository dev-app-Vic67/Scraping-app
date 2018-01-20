from urllib.request import urlopen, URLError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import random
import datetime


random.seed(datetime.datetime.now())

def getInternalLinks(bsObj, includeUrl):
    """Get all internal links on page"""
    includeUrl = urlparse(includeUrl).scheme + '://' + urlparse(includeUrl).scheme
    internalLinks = []
    # find all links begining from '/'
    try:
        links = bsObj.find_all('a', href=re.compile("^(/|.*" + includeUrl + ")"))
    except AttributeError as error:
        print(error)
        return None
    else:
        for link in links:
            if link.attrs['href'] is not None:
                if link.attrs['href'] not in internalLinks:
                    internalLinks.append(link.attrs['href'])

    return internalLinks


def getExternalLinks(bsObj, exludeUrl):
    """Get all external links from page"""
    externalLinks = []
    # find all links begining from 'http', 'www' and not inlcude current URL
    try:
        links = bsObj.find_all('a', href=re.compile("^(http|www)((?!" + exludeUrl + ").)*$"))
    except AttributeError as error:
        print(error)
        return None
    else:
        for link in links:
            if link.attrs['href'] is not None:
                if link.attrs['href'] not in externalLinks:
                    externalLinks.append(link.attrs['href'])

    return externalLinks


def getRandomExternalLink(startingPage):
    """Get random external links"""
    try:
        html = urlopen(startingPage)
    except URLError as error:
        print(error)
        return None
    try:
        bsObj = BeautifulSoup(html, 'lxml')
        externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)
    except AttributeError as error:
        print(error)
        return None
    else:
        if len(externalLinks) == 0:
            print('No external links, looking around the site for one')
            domain = urlparse(startingPage).scheme + '://' + urlparse(startingPage).netloc
            print(startingPage)
            print(domain)
            internalLinks = getInternalLinks(bsObj, domain)
            return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks) - 1)])
        else:
            return externalLinks[random.randint(0, len(externalLinks) - 1)]


def followExternalOnly(startingSite):
    """"""
    externalLink = getRandomExternalLink(startingSite)
    print('Random external link is:', externalLink)
    followExternalOnly(externalLink)


allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
    try:
        html = urlopen(siteUrl)
        domain = urlparse(siteUrl).scheme + '://' + urlparse(siteUrl).netloc
    except URLError as error:
        print(error)
    try:
        bsObj = BeautifulSoup(html, 'lxml')
    except AttributeError as error:
        print(error)
    else:
        internalLinks = getInternalLinks(bsObj, domain)
        externalLinks = getExternalLinks(bsObj, domain)

        for link in externalLinks:
            if link not in allExtLinks:
                allExtLinks.add(link)
                print(link)
        for link in internalLinks:
            if link not in allIntLinks:
                allIntLinks.add(link)
                getAllExternalLinks(link)


followExternalOnly('http://oreilly.com')

allIntLinks.add('http://oreilly.com')
getAllExternalLinks('http://oreilly.com')
