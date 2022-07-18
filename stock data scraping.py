# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 13:07:24 2022

@author: akhil
"""

import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.marketwatch.com/investing/stock/tsla?mod=search_symbol'
page = requests.get(url)
page

soup = BeautifulSoup(page.text,'lxml')
soup

#price of stock
price = soup.find('bg-quote', class_ = 'value').text
price

#closing price of stock
cprice = soup.find('td', class_ = 'table__cell u-semi').text
cprice

#52 week range
nested = soup.find('mw-rangebar',class_ = 'element element--range range--yearly')
nested

lower = nested.find_all('span',class_ = 'primary')[0].text
lower

higher = nested.find_all('span',class_ = 'primary')[1].text
higher

#analyst rating
Arating = soup.find('li', class_ = 'analyst__option active').text
Arating
