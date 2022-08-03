# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 08:54:45 2022

@author: akhil
"""

import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.moneycontrol.com/india/stockpricequote/diversified/itc/ITC'
page = requests.get(url)
page

soup = BeautifulSoup(page.text,'lxml')
soup

#price of stock
price = soup.find('div', class_ = 'inprice1 nsecp').text
price

#previous close price of stock
pvcprice = soup.find('td', class_ = 'nseprvclose bseprvclose').text
pvcprice

#52 week range
lower = soup.find('div', class_ = 'FL nseL52').text
lower

upper = soup.find('div', class_ = 'FR nseH52').text
upper
