import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Accept-Language': 'en-US, en;q=0.5'
}
base_url = "https://www.flipkart.com/realme-c35-glowing-black-64-gb/p/itmafb045222b2cf?pid=MOBGBTHFDQXQEGNS&lid=LSTMOBGBTHFDQXQEGNSZWXHXJ&marketplace=FLIPKART&q=realme+c35+mobile&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&fm=Search&iid=886c242c-d713-49c2-96ed-269c1907807e.MOBGBTHFDQXQEGNS.SEARCH&ppt=pp&ppn=pp&ssid=4n9i3t8nkg0000001652237157273&qH=eb8a5aaa14d24e12"
def flipkart_prodect(base_url)->dict:
    try:
        res = requests.get(base_url)
    except:
        return {"error":"invalid url"}
    soup = BeautifulSoup(res.text,"html.parser")
    title = soup.find("span",{"class":"B_NuCI"}).text
    price = soup.find("div",{"class":"_30jeq3 _16Jk6d"}).text
    image=  soup.find("img",{"class":"q6DClP"})['src']

    try:
        description = soup.find("div",{"class":"_1mXcCf RmoJUa"}).p.text
    except:
        description = ""
        pass
    
    
    
    return {
        "title":title,
        "url":base_url,
        "price": price,
        "description": description,
        "image":image,
        "error":False
            
    }

# print(soup(base_url))