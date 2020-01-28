'''
Created on 2020. 1. 14.

@author: GDJ_19
lambdaex1.py : 람다식으로 함수 구현하기
 람다 : 함수객체
       함수의 기능도 동적으로 처리하겠다.
     함수가 정의되면 고정된 기능만 할 수 있는데, 람다는 동적으로 변경할 수 있다.
'''
def hap(num1,num2):
    res = num1 + num2
    return res
print(hap(10,20))

hap2 = lambda num1,num2:num1+num2
print(hap2(10,20))

hap3 = lambda num1,num2:num1*num2
print(hap3(10,20))

#매개변수에 기본값 설정하기
hap4 = lambda num1=0,num2=0 : num1+num2
print(hap4())
print(hap4(100))
print(hap4(100,200))
