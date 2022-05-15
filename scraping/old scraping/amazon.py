import requests
from bs4 import BeautifulSoup
import os 
os.system("cls")
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

# URL  = "https://www.amazon.in/s?k=tv&crid=3JFFIA59SM1KU&sprefix=tv%2Caps%2C384&ref=nb_sb_noss_1"

# response = requests.get(URL, headers=headers)

# soup = BeautifulSoup(response.text,"html.parser")


page_class =  []
name_class = []
result = [] 
products  =[]


# products = soup.find_all("div",{"class":"s-card-container s-overflow-hidden aok-relative s-include-content-margin s-latency-cf-section s-card-border"})
# for product in products:
    
#     name = product.find("span",{"class":"a-size-medium a-color-base a-text-normal"})
#     if bool(name):
#         price = product.find("span",{"class":"a-price-whole"})
#         if bool(price):
#             result.append({"name":name.text,"price":price.text}) 
    
    

# print(f"products = {len(products)}")
# print(f"result = {len(result)}")
# for product in result: 
#     print(product)



def product_info(url):
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text,"html.parser")
        name=soup.find("span",{"class":"a-size-large product-title-word-break"})
        price=soup.find("span",{"class":"a-offscreen"})
        
        # about =soup.find("ul",{"class":"a-unordered-list a-vertical a-spacing-mini"})

        return {
            "name":name.text,
            "price":price.text,
            # "about":about.text
        }
        
        
    except:
        print("Invalied url")

print(product_info("https://www.amazon.in/Preethi-Flame-Sparkle-Glass-3-Burner/dp/B00TK5IFQ2/ref=sr_1_2_sspa?keywords=gas+stove+3+burners&qid=1652546634&sprefix=ga,aps,484&sr=8-2-spons&psc=1"))