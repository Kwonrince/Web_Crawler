# -*- coding: utf-8 -*-
"""
Created on Mon May  2 15:47:35 2022

@author: 201
"""

from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.youtube.com/watch?v=_MYR9Dp8Eys")
driver.implicitly_wait(3)

time.sleep(1.5)

driver.execute_script("window.scrollTo(0, 800)")
time.sleep(3)

# 페이지 끝까지 스크롤
last_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(5)

    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

time.sleep(5)

# 팝업 닫기
try:
    driver.find_element_by_css_selector("#dismiss-button > a").click()
except:
    pass

# 대댓글 모두 열기
# buttons = driver.find_elements_by_css_selector("#more-replies > a")

# time.sleep(3)

# for button in buttons:
#     button.send_keys(Keys.ENTER)
#     time.sleep(5)
#     button.click()

# time.sleep(1.5)

# 정보 추출하기
html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')

id_list = soup.select("div#header-author > h3 > #author-text > span")
comment_list = soup.select("yt-formatted-string#content-text")


id_final = []
comment_final = []

for i in range(len(comment_list)):
    temp_id = id_list[i].text
    temp_id = temp_id.replace('\n', '')
    temp_id = temp_id.replace('\t', '')
    temp_id = temp_id.replace('    ', '')
    id_final.append(temp_id)

    temp_comment = comment_list[i].text
    temp_comment = temp_comment.replace('\n', '')
    temp_comment = temp_comment.replace('\t', '')
    temp_comment = temp_comment.replace('    ', '')
    comment_final.append(temp_comment)

pd_data = {"아이디" : id_final , "댓글 내용" : comment_final}
youtube_pd = pd.DataFrame(pd_data)
# convert_csv_from_dataframe('title',youtube_pd)
# youtube_pd.to_excel('youtube.xlsx',encoding = 'cp949')
youtube_pd.to_csv(f"./data/youtube_pd_title_5.csv", encoding='utf-8-sig')
driver.close()
# 104개 중에서 104개 모두 읽힘 
