from bs4 import BeautifulSoup as bsoup
from urllib2 import urlopen
import requests as rq
import re

urls = ["http://www.example.com", 'www.example1.com']
for page in urls:
    sauce = urlopen(page).read()
    soup = bsoup(sauce, 'lxml')
    print soup

