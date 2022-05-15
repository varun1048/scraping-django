from .constant import flipkart, FlipkartLiterals, Scrap
from bs4 import BeautifulSoup, Tag, NavigableString
from .constant import get_url

def getTextFromSoup(soup):
    if(soup):
        return soup.text
    else:
        return ''

def getImageSrcFromSoup(soup):
    if(soup):
        return str(soup["src"])
    else:
        return ''

def getURLFromSoup(soup):
    if(soup):
        return "https://www.flipkart.com"+ str(soup["href"])
    else:
        return ''

def validateSoup(soup):
    if soup != None:
        return True
    else:
        return False

def getTitleWithDivAndClass(soup : BeautifulSoup) -> str:
    title = ''
    for titleClass in flipkart.get(FlipkartLiterals.TITLE.value):
        souped = soup.find('div', attrs= { 'class' : titleClass })
        if(validateSoup(souped)):
            title = souped
            break
        
        souped = soup.find('a', attrs= { 'class' : titleClass })
        if(validateSoup(souped)):
            title = souped
            break
        
    return getTextFromSoup(title)

def getImageWithDivAndClass(soup : BeautifulSoup) -> str:
    image = ''
    for imgClass in flipkart.get(FlipkartLiterals.IMAGE.value):
        souped = soup.find("img", attrs={"class": imgClass})
        if(validateSoup(souped)):
            image = souped
            break
    return getImageSrcFromSoup(image)

def getPriceWithDivAndClass(soup : BeautifulSoup) -> str:
    price = ''
    for priceClass in flipkart.get(FlipkartLiterals.PRICE.value):
        souped = soup.find('div', attrs= { 'class' : priceClass })
        if(validateSoup(souped)):
            price = souped
            break
    return getTextFromSoup(price)

def getURLWithDivAndClass(soup : BeautifulSoup) -> str:
    url = ''
    for urlClass in flipkart.get(FlipkartLiterals.URL.value):
        souped = soup.find('a', attrs= { 'class' : urlClass })
        if(validateSoup(souped)):
            url = souped
            break
    return getURLFromSoup(url)

def getDescriptionWithDivAndClass(soup : BeautifulSoup) -> str:
    desc = ''
    for descClass in flipkart.get(FlipkartLiterals.DESCRIPTION.value):
        souped = soup.find("ul", attrs={"class": descClass})
        if(validateSoup(souped)):
            desc = souped
            break
    return getTextFromSoup(desc)


def makeScrap(soup : BeautifulSoup) -> Scrap:
    return {
        'title' : getTitleWithDivAndClass(soup),
        'image' : getImageWithDivAndClass(soup),
        'description' : getDescriptionWithDivAndClass(soup),
        'price' : getPriceWithDivAndClass(soup),
        'url' : getURLWithDivAndClass(soup)
    }

def flipkartScraping(url : str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
        'Accept-Language': 'en-US, en;q=0.5'
    }
    data = []
    res = get_url(url, headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    for page in flipkart.get(FlipkartLiterals.PAGE.value):
        for s in soup.find_all('div', attrs = { 'class' : page}):
            data += [makeScrap(s)]
    
    return data
