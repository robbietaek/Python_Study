'''
Created on 2020. 1. 9.

@author: GDJ_19
    input(), print() 함수
    input("입력전 출력 문자열") 함수는 기본적으로 문자열을 입력 받는다.
    print(출력값1, 출력값2, ...) 함수는 여러개 출력시 ,로 연결이 가능하다.
'''
a = int(input("값 1 입력"))
b = int(input("값 2 입력"))
result = a+b
print(a ,"+", b, "=",result)
print("%d + %d = %d" % (a,b,result))

print("안녕하세요 ", end ="") #end라는 속성 자체가 new line 이므로 그것을 없애줌.
print("홍길동입니다.", end = ":")
print("반가워요")

#format 함수 사용하기
print("{0:d} {1:5d} {2:05d}".format(100, 200, 300)) #0번째를 한자리 확보 1번째는 5자리확보 2자리는 빈자리 5으로 채워서 5자리확보
print("{2:d} {1:5d} {0:05d}".format(100, 200, 300)) #0번째를 한자리 확보 1번째는 5자리확보 2자리는 빈자리 5으로 채워서 5자리확보