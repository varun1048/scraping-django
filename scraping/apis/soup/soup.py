from constant import amazon,flipkart
from bs4 import BeautifulSoup

def web_scraping_using_classes(classes, source):
    soup = BeautifulSoup(source,"html.parser")