import enum
from typing import TypedDict

class Scrap(TypedDict):
    title : str
    image : str
    url : str
    price : str
    description : str


class FlipkartLiterals(enum.Enum):
    TITLE = 'titleClasses'
    PRICE = 'priceClasses'
    DESCRIPTION = 'descClasses'
    IMAGE = 'imageClasses'
    URL = 'urlClasses'
    PAGE = 'pageClasses'

flipkart = {
    "titleClasses" : ["_4rR01T","_1W9f5C","s1Q9rs","IRpwTa",],
    "priceClasses" : ["_30jeq3"],
    "descClasses" : ["_1xgFaf"],
    "imageClasses" : ["_2r_T1I","_396cs4 _3exPp9","_396cs4 _3exPp9"],
    "urlClasses" : ["s1Q9rs","_1fQZEK","_2UzuFa"],
    "pageClasses" : ["_2rpwqI","_6WQwDJ","_4ddWXP","_2kHMtA","_1xHGtK _373qXS","_2nRPpA"]
}

from urllib.error import HTTPError
import requests

def get_url(url : str, headers : dict):
    try:
        res = requests.get(url,headers = headers)
    except:
        raise HTTPError(url, 404, "Invalid URL", headers)
    return res
    

