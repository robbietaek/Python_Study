'''
Created on 2020. 1. 9.

@author: GDJ_19
삼각형을 출력하기
'''

num = int(input("숫자를 입력하세요"))

for i in range(1,num+1) :
    print("*"*i)
    
print("")    
    
for i in range(num,0,-1) :
    print("*"*i)    
    
for i in range(0,num+1) :
    print(" "*(num-i)+"*"*(i))
    
for i in range(0,num+1) :
    print(" "*(num-i)+"*"*(i)+"*"*(i-1))