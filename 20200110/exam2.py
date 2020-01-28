'''
Created on 2020. 1. 10.

@author: GDJ_19
'''

ss = "홍길동"
#홍#길#동 으로 출력하기

for i in range(0,len(ss)) :
    print(ss[i],end="#")
    
print()

#동길홍으로 출력하기    
print(ss[::-1])    

# ss 문자열이 (로 시작하지 않으면 (를 추가하기, (시작하면 추가

if ss.startswith("(") ==False :
    print("(",end="")
print(ss,end="")
if ss.endswith(")") == False :
    print(")")
    
    
ss = "2020/01/10"        
print("ss 날짜의 10년 전을 출력하기")
list = ss.split("/")
list[0] = int(list[0])-10
print(list)
