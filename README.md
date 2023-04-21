# Web_Crawler
naver news, naver blog, daum news, youtube crawler 입니다.

jupyter notebook(`.ipynb`)에서 실행 결과를 확인할 수 있습니다.

웹 크롤링에 대한 가이드 자료는 [웹 크롤링 가이드](./slides/crawling_guide.pdf)에서 확인할 수 있습니다.

## Usage
필요한 library 설치

```bash
$ pip install selenium, beautifulsoup4, requests
```

selenium library를 사용하기 위한 현재 사용중인 브라우저 버전에 맞는 web driver 다운 필요(가이드 19페이지 참조)
- [Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
- [Chrome WebDriver](https://chromedriver.chromium.org/downloads)

크롤링한 데이터는 기본적으로 `./data/` 안에 저장되므로 디렉토리 생성 필요
```bash
$ mkdir data
```

-------------------
** Contributor    
Soonki Kwon : kwonrince@gmail.com       
Hyunho Lee : lake8000@ds.seoultech.ac.kr
