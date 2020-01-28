'''
Created on 2020. 1. 9.

@author: GDJ_19
숫자를 입력받아 입력수까지 합을 출력하기
숫자를 입력받아 입력수까지 짝수의 합을 출력하기
숫자를 입력받아 입력수까지 홀수의 합을 출력하기
'''
total = 0
num = int(input('숫자를입력하세요'))

for i in range(1,num+1) :
    total += i

print(total)


total = 0;

for i in range(0,num+1,2) :
    total += i

print(total)

total = 0;

for i in range(1,num+1,2) :
    total += i

print(total)