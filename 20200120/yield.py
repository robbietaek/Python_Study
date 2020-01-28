'''
Created on 2020. 1. 20.

@author: GDJ_19
yieldex1.py : 함수의 종료 없이, yield 예약어로 값 리턴
'''
def genFun(num):
    for i in range(10, num+10) :
        yield(i)            #중간중간 값을 계속해서 전달해준다.
        print(i, "값 반환")

print(type(genFun(5))) #generator 로 된다.
print(list(genFun(5)))  #list 로 형변환 해야 볼 수 있다.

for i in list(genFun(5)) :      #yield
    print(i)