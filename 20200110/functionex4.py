'''
Created on 2020. 1. 10.

@author: GDJ_19
functionex4.py : 1. 리턴값을 두개 반환하기 : 리스트로 반환
                 2. 가변매개변수 함수 정의
'''

def multi(a,b):
#     hap = a+b
#     sub = a-b
#     list = [hap,sub]
#     return list
    return [a+b,a-b]

def paramFunc(* p): #0개 이상 매개변수
    result = 0;
    for i in p :
        result += i
    return result

list = []
hap,sub = 0,0
list = multi(100,200)
hap = list[0]
sub = list[1]
print("multi 함수의 리턴값 : %d, %d " % (hap,sub))

# 가변 파라미터 연습
print("paramFunc(10,20)=",paramFunc(10,20)) #파라미터가 여러개여도 된다.
print("paramFunc(10,20,30)=",paramFunc(10,20,30))   #파라미터의 개수가 달라도 된다.