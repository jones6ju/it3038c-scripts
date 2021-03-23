import requests, re
from bs4 import BeautifulSoup

r = requests.get("https://www.nike.com/w/mens-jordan-shoes-37eefznik1zy7ok").content
soup = BeautifulSoup(r, 'html.parser')
d = soup.findAll("div", {"data-test":"product-price"})

print(d)