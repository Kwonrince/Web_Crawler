# -*- coding: utf-8 -*-
"""
Created on Mon May  2 16:48:51 2022

@author: 201
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup

res = requests.get("https://news.daum.net/")

soup = BeautifulSoup(res.content, 'html.parser')

items = soup.select('div strong a')





title=[]
url = []

for i in range(len(items)):
    
    title.append(items[i].text.strip())
    url.append(items[i].attrs['href'])

list_sum = list(zip(title,url))

col = ['title','url']

df = pd.DataFrame(list_sum, columns=col)
df.to_csv('daum_new.xlsx', sheet_name='뉴스 기사 제목')
