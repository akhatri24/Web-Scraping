# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 16:29:36 2022

@author: akhil
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.nfl.com/standings/league/2021/REG'
page = requests.get(url)
page

soup = BeautifulSoup(page.text, 'lxml')
soup

table = soup.find('table',{'summary':'Standings - Detailed View'})
table

table.find_all('th')

headers = []
for i in table.find_all('th'):
    title = i.text.strip()
    headers.append(title)
    
nfl_standings = pd.DataFrame(columns=headers)

table.find_all('tr')[1:]

for row in table.find_all('tr')[1:]:
    first_td = row.find_all('td')[0].find('div',class_='d3-o-club-fullname').text.strip()
    data = row.find_all('td')[1:]
    row_data = [td.text.strip() for td in data]
    row_data.insert(0,first_td)
    length = len(nfl_standings)
    nfl_standings.loc[length] = row_data
    
nfl_standings.to_csv(r"C:\Users\akhil\OneDrive\Documents\Data Analytics\Udemy\NFL_Standings_2021.csv")
