'''
Created on 2020. 2. 7.

@author: GDJ_19
xml 파일을 읽어 분석하기
'''
from bs4 import BeautifulSoup
import urllib.request as req
import os.path
#forecast.xml 파일을 읽어 xml 값에 저장하기
#날씨구분으로 도시들을 저장
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
if not os.path.exists("forecast.xml") : #만약 파일이 없으면
    req.urlretrieve(url, "forecast.xml")    #url로부터 forecast.xml 이라는 파일을 만들어라
    
xml = open("forecast.xml","r",encoding="utf-8").read()
info = {}   #dictionary 사용
soup = BeautifulSoup(xml, "html.parser")
for location in soup.find_all("location") :
    name = location.find("city").string
    weather = location.find("wf").string
    if not (weather in info) :
        info[weather] = []
    info[weather].append(name)
for weather in info.keys() :
    print("+",weather)
    for name in info[weather] :
        print("| - ",name)