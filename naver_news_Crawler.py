
from bs4 import BeautifulSoup
import requests
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)


# 페이지 url 형식에 맞게 바꾸어 주는 함수 만들기
# 입력된 수를 1, 11, 21, 31 ...만들어 주는 함수


# 크롤링할 url 생성하는 함수 만들기(검색어, 크롤링 시작 페이지, 크롤링 종료 페이지)


def makePgNum(num):
    if num == 1:
        return num
    elif num == 0:
        return num + 1
    else:
        return num + 9 * (num - 1)


def makeUrl(search, start_pg, end_pg):
    if start_pg == end_pg:
        start_page = makePgNum(start_pg)
        url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(
            start_page)
        print("생성url: ", url)
        return url
    else:
        urls = []
        for i in range(start_pg, end_pg + 1):
            page = makePgNum(i)
            url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(page)
            urls.append(url)
        print("생성url: ", urls)
        return urls


##########뉴스크롤링 시작###################

# 검색어 입력
search = input("검색할 키워드를 입력해주세요:")

# 검색 시작할 페이지 입력
page = int(input("\n크롤링할 시작 페이지를 입력해주세요. ex)1(숫자만입력):"))  # ex)1 =1페이지,2=2페이지...
print("\n크롤링할 시작 페이지: ", page, "페이지")
# 검색 종료할 페이지 입력
page2 = int(input("\n크롤링할 종료 페이지를 입력해주세요. ex)1(숫자만입력):"))  # ex)1 =1페이지,2=2페이지...
print("\n크롤링할 종료 페이지: ", page2, "페이지")

# naver url 생성
search_urls = makeUrl(search, page, page2)

## selenium으로 navernews만 뽑아오기##
driver = webdriver.Chrome('chromedriver.exe')
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
driver.implicitly_wait(3)


naver_urls = []
count = 0  # 

for i in search_urls:
    driver.get(i)
    time.sleep(1) 

    a = driver.find_elements(By.CSS_SELECTOR, 'a.info')

    for i in a:
        count += 1
        i.click()

        # 현재탭에 접근
        driver.switch_to.window(driver.window_handles[count - 1])
        time.sleep(3)  

        url = driver.current_url
        print(url)

        if "news.naver.com" in url:
            naver_urls.append(url)

        else:
            pass
        driver.switch_to.window(driver.window_handles[0])
print(naver_urls)

###naver 기사 본문 및 제목 가져오기###

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/98.0.4758.102"}

titles = []
contents = []
for i in naver_urls:
    original_html = requests.get(i, headers=headers)
    html = BeautifulSoup(original_html.text, "html.parser")


    title = html.select("div#ct > div.media_end_head.go_trans > div.media_end_head_title > h2")
    title = ''.join(str(title))
    pattern1 = '<[^>]*>'
    title = re.sub(pattern=pattern1, repl='', string=title)
    titles.append(title)

    content = html.select("div#dic_area")
    content = ''.join(str(content))
    content = re.sub(pattern=pattern1, repl='', string=content)
    pattern2 = """[\n\n\n\n\n// flash 오류를 우회하기 위한 함수 추가\nfunction _flash_removeCallback() {}"""
    content = content.replace(pattern2, '')
    contents.append(content)

print(titles)
print(contents)


import pandas as pd

news_df = pd.DataFrame({'title': titles, 'link': naver_urls, 'content': contents})

news_df

news_df.to_csv('./data/NaverNews_%s.csv' % search, index=False, encoding='utf-8-sig')
