'''
Created on 2020. 2. 7.

@author: GDJ_19
'''
from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)
soup = BeautifulSoup(res,"html.parser",from_encoding="euc-kr")
hlist = soup.select("div.head_info")
htitle = soup.select("h3.h_lst")
for tag, title in zip(hlist,htitle) :
    print(title.select_one("span.blind").string, end = "\t")
    value = tag.select_one("span.value").string
    print(value, end = " ")
    change = tag.select_one("span.change").string
    print(change, end = "\t")
    
    blinds = tag.select("span.blind")
    b = tag.select("span.blind")[-1].string
    print(b, end="********\n")
