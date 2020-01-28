'''
Created on 2020. 1. 14.

@author: GDJ_19
try, exception
'''

mystr = "파이썬 공부중 입니다. 열심히 파이썬 공부를 합시다."
strpos = []
index = 0
while True :
    try :
        index = mystr.index("파이썬",index) #뒤에 index 를 넣어주면 인덱스 이후의 파이썬 문자열 위치를 알려준다.
        print(index)
        strpos.append(index)
        index += 1
    except :
        break
print("파이썬의 문자 위치 :",strpos,",문자갯수",len(strpos))
