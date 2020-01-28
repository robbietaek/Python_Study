'''
Created on 2020. 1. 20.

@author: GDJ_19
정규식예제 2, 정규화 모듈 사용하기
정규식 표현법
    () : 그룹화
    [] : 문자
    {} : 개수
    \d : 숫자
    
    (\d{6})[-]\d{7}    : 첫번째 그룹 : 숫자 6자리, 다음문자가 - 이면서, 다음문자는 숫자 7자리로 이루어진 문자열
    \g<1>-******* : \g<1> 첫번째 그룹
    
    ? : 0 또는 1 개
    ca?t : a 문자가 없거나 1개인 경우 True
            "ct" : True
            "cat" : True
            "caaaat" : False
    * : 0개 이상
    ca*t : a 문자가 없거나 여러개인 경우
            "ct" : True
            "cat" : True
            "caaaat" : True
            
    + : 1개 이상
        ca+t : a 문자가 1개이거나 여러개인 경우
                "ct" : False
                "cat" : True
                "caaaat" : True
                
    {n} : n개 반복
        ca{2}t : a 문자가 2개
                "ct" : False
                "cat" : False
                "caaaat" : False                            
                "caat" : True
                
    {n,m} : n개 이상 m개 까지
        ca{2,5}t : a 문자가 2개 이상 5개 이하
                "ct" : False
                "cat" : False
                "caaaat" : True                            
                "caat" : True
                "caaaaaaat" False                
'''

import re

data = '''
    park 800905-1234567
    kim 700905-1234567
    choi 850114-a123456
'''
pat = re.compile("(\d{6})[-]\d{7}")     #조건문
print(pat.sub("\g<1>-*******",data))    #조건에 맞는 애들을 변경해라