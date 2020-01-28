'''
Created on 2020. 1. 14.

@author: GDJ_19
'''
def fibo(n):
    global fibolist
    fibolist = [0,1]
    for i in range(1,n-1) :
        fibolist.append(fibolist[i-1]+fibolist[i])
    
fibolist = []
num1 = 0
num2 = 1
num3 = num1+num2
num = int(input("피보나치 수열을 구할 갯수를 입력하세요. 단 3 이상의 값"))
print("f(",num,")=",end="")
fibo(num)
print(fibolist)