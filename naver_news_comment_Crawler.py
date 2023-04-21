# -*- coding: utf-8 -*-
"""
Created on Sun May  8 12:16:27 2022

@author: 이현호
"""

from selenium import webdriver
import time
import pandas as pd
from bs4 import BeautifulSoup

driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(5)
driver.get('https://n.news.naver.com/mnews/article/001/0013158930?sid=105')

while True:
    try:
        more = driver.find_element_by_css_selector('a.u_cbox_btn_more')
        more.click()
        time.sleep(0.1)

    except:
        break

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

nicknames = soup.select('span.u_cbox_nick')
list_nicknames = [nickname.text for nickname in nicknames]

datetimes = soup.select('span.u_cbox_date')
list_datetimes = [datetime.text for datetime in datetimes]

contents = soup.select('span.u_cbox_contents') 
list_contents = [content.text for content in contents]

list_sum = list(zip(list_nicknames,list_datetimes,list_contents))


driver.quit()


list_sum


col = ['작성자','시간','내용']

# pandas 데이터 프레임 형태로 가공
df = pd.DataFrame(list_sum, columns=col)

# 데이터 프레임을 엑셀로 저장 (파일명은 'news.xlsx', 시트명은 '뉴스 기사 제목')
df.to_excel('naver_news_comment.xlsx', sheet_name='뉴스 기사 제목')
