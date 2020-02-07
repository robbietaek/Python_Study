'''
Created on 2020. 2. 7.

@author: GDJ_19
크롤링예제
'''
from bs4 import BeautifulSoup   #html 분석 모듈
import urllib.request as req    #url 사용 모듈
url =\
"http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
res = req.urlopen(url)  #url 전달된 데이터. soup의 분석 대상 데이터
soup = BeautifulSoup(res,"html.parser") #Beautiful 객체
title = soup.find("title").string   #title 태그와 내용
wf = soup.find("wf").string
print(title)
print(wf)
