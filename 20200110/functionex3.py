'''
Created on 2020. 1. 10.

@author: GDJ_19
functionex3.py : 전역변수 사용하기
'''

def func1():
    global gval
    gval = 200
    a = 200 #지역변수다
    b = 1000 #지역변수다
    print("func1() 함수 호출함",gval,a,b)

def func2():
    print("func2() 함수에서 func1() 함수를 호출함")
    func1()
    print("전역 변수 gval 값 = ",gval,a)
    
gval = 100  #전역변수=> 모든함수에서 사용이 가능한 변수
a = 10  #전역변수
if __name__ == '__main__' : #프로그램의 시작
    func2()    