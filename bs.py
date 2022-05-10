import requests
from bs4 import BeautifulSoup

url = "https://hamrobazaar.com/"

response = requests.get(url)
print(response.status_code) 
