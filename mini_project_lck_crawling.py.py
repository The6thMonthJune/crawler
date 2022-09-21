from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
service = Service(executable_path="chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(service=service, options=options)
# kewd = input('어떤 주제로 검색을 할까요? : ')
# que = input('몇 페이지를 크롤링 할까요?(1페이지에 10개) : ')
url = 'https://www.bigkinds.or.kr/'
browser.get( url )
element = browser.find_element(By.XPATH, '//*[@id="total-search-key"]') #검색창 선택
element.send_keys('lck') #검색어 설정
element.send_keys('\n') # 검색
f = open('text.txt', 'w', encoding='utf-8') # utf-8 형식으로 text.txt에 저장

for i in range(1, 30): #1페이지부터 30페이지까지 반복
    elements = browser.find_elements(By.CSS_SELECTOR, 'span.title-elipsis') #기사 제목을 elements에 저장
    for element in elements: #기사 제목들 선택을 반복
        try:
            element.click() # 제목 선택
            time.sleep(1) #1초 대기
            article = browser.find_element(By.XPATH, '//*[@id="news-detail-modal"]/div/div/div[1]/div/div[2]') #article에 출력
            f.write(article.text) #article.text에 작성
            button = browser.find_element(By.XPATH, '//*[@id="news-detail-modal"]/div/div/button') #닫기(x)버튼 찾기
            button.click() #닫기 버튼 클릭
        except: #예외
            try: 
                button = browser.find_element(By.XPATH, '//*[@id="news-detail-modal"]/div/div/button') #닫기 버튼을 다시 탐색
                button.click() #닫기 버튼 클릭
            except:
                pass #지나쳐줘
    button = browser.find_element(By.XPATH, '//*[@id="paging_news_result"]')   # 페이지 번호 검색창 선택
    button.clear() #페이지 번호 제거
    button.click() #페이지 번호 검색창 클릭
    button.send_keys(i+1) #페이지 번호 작성 (i+1) : 1씩 증가
    button.send_keys('\n') #검색
    time.sleep(1) #1초 대기
f.close() #text.txt 파일 닫기
browser.quit() #브라우저 종료