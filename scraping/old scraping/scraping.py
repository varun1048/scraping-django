import requests
from bs4 import BeautifulSoup
import os
os.system("cls")

def  scrape_flipkart(base_url)->list:
    # base_url = "https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
        'Accept-Language': 'en-US, en;q=0.5'
    }
    try:
        response = requests.get(base_url,headers=headers)
        print(f"response {response.status_code}")
        soup = BeautifulSoup(response.text, "html.parser")
    except:
        print("Invalid URl")
        return []

    data = []
    def get_title(souped)->str:
        title_class = ["_4rR01T","_1W9f5C","s1Q9rs","IRpwTa",]
        for tag in ["div","a"]:
            for name in title_class:        
                title = souped.find(tag, attrs={"class": name})
                if title:
                    return  str(title.text)
        return "None"

    def get_price(souped)->str:
        price_class = ["_30jeq3"]
        for name in price_class:        
            price = souped.find("div", attrs={"class": name})
            if price:
                return  str(price.text)
        return "None"

    def get_url(souped)->str:
        url_class = ["s1Q9rs","_1fQZEK","_2UzuFa"]

            
        for name in url_class:        
            url = souped.find("a", attrs={"class": name})
            if url:
                return "https://www.flipkart.com"+ str(url["href"])

        return "None"
    def get_img(souped)->str:
        img_class = ["_2r_T1I","_396cs4 _3exPp9","_396cs4 _3exPp9"]
        for name in img_class:        
            img = souped.find("img", attrs={"class": name}) 
            if img:
                return  str(img["src"])
        return "None"


    def get_description(souped)->str:
        get_description_class = ["_1xgFaf"]
        for name in get_description_class:        
            get_description = souped.find("ul", attrs={"class": name})
            if get_description:
                return  str(get_description.text)
        return "None"


    
    page_class = ["_2rpwqI","_6WQwDJ","_4ddWXP","_2kHMtA","_1xHGtK _373qXS","_2nRPpA"]

    for page in page_class:
        for souped in  soup.find_all("div", attrs={"class": page}):
            title = get_title(souped)
            url = get_url(souped)
            price = get_price(souped)
            description = get_description(souped)
            img = get_img(souped)
            if (    (title and   url) and (price and description) ) and img:
                data += [{
                    # "souped ":souped ,
                    # "page":page ,
                    "url":url,
                    "price":price,
                    "title":title,
                    "description":description,
                    "img":img
                } ]

    return data

# output = scrape_flipkart("https://www.flipkart.com/search?q=cd+player&sid=0pm%2Cw7f&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=cd+player%7CVideo+Players+%26+Recorders&requestId=bb2ada15-10ff-49f3-b547-bc71bba285a0&as-backfill=on")
# print(len(output))