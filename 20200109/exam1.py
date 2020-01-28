'''
Created on 2020. 1. 9.

@author: GDJ_19

exam1.py = 금액을 입력받아 필요한 동전의 갯수를 구하시오
단 동전은 500, 100, 50, 10, 1의 종류가 있다.
각각 동전의 갯수를 구하시오
'''


money = int(input("금액을 입력하세요"))
left = 0

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

count1 = money//500
left =money%500

count2 = left//100
left =left%100

count3 = left//50
left =left%50

count4 = left//10

count5 =left%10

print('500원 동전의 갯수 :',count1)
print('100원 동전의 갯수 :',count2)
print('50원 동전의 갯수 :',count3)
print('10원 동전의 갯수 :',count4)
print('1원 동전의 갯수 :',count5)
 


