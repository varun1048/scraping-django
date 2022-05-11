import requests
from bs4 import BeautifulSoup
import os
os.system("cls")

first_page_url = "https://www.flipkart.com/search?q=swimming+pool&sid=tng%2Clhf%2Cjxi&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=swimming+pool%7CSwimming+Pool&requestId=14637aea-84da-4b7d-b702-f8007d25fc43&as-backfill=on"
response = requests.get(first_page_url)
print(f"response {response.status_code}")
soup = BeautifulSoup(response.text, "html.parser")


def soup_page(url)->list:
    pages = []
    
    response = requests.get(url)
    print(f"response {response.status_code}")
    soup = BeautifulSoup(response.text, "html.parser")
    pages.append(soup)
    
    #for next page 
    for x in range(2):
        soup_page(pages)
        

    return soup

# lenght = len(soup_page(first_page_url))
print(soup_page(first_page_url))








# def page_two():
#     data = []
#     out = soup.find_all("div", attrs={"class": "_4ddWXP"})
#     for x in out:
#         url_and_title = x.find("a", attrs={"class": "s1Q9rs"})
#         prise = x.find("div", attrs={"class": "_30jeq3"})
#         # description = x.find_all("li", attrs={"class": "rgWa7D"})
#         # print(x)
#         # print("/n")
#         # print("/n")
#         data.append({
#             "url": "https://www.flipkart.com"+url_and_title["href"],
#             "title": url_and_title.text,
#             "prise": prise.text,
#             # "description": "".join(map(lambda y: y.text, description))
#         })

#     for x in data[0:2]:
#         print(x)
        
           
#     print(f"len {len(out)} ")

# # page_two()
















def page_one():
    data = []
    out = soup.find_all("a", attrs={"class": "_1fQZEK"})
    for x in out:
        url = x["href"]
        name = x.find("div", attrs={"class": "_4rR01T"})
        prise = x.find("div", attrs={"class": "_30jeq3 _1_WHN1"})
        description = x.find_all("li", attrs={"class": "rgWa7D"})

        data.append({
            "url": "https://www.flipkart.com"+url,
            "title": name.text,
            "prise": prise.text,
            "description": "".join(map(lambda y: y.text, description))
        })

    for x in data[0:4]:
        print(x)
    
    print(f"len {len(out)} ")

page_one()