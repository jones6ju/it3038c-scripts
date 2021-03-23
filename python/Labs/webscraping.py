from bs4 import BeautifulSoup
import requests, re

r = requests.get('https://analytics.usa.gov').content

soup = BeautifulSoup(r, "lxml")
