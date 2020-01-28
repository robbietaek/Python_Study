'''
Created on 2020. 1. 9.

@author: GDJ_19
strex1.py : 문자열 처리하기
        문자열을 배열로 처리할 수 있다.
'''
from test.test_wsgiref import hello_app
from trace import _find_strings

print("안녕하세요")  #안녕하세요
print("안녕하세요"[0])   #안 (앞에서부터 출력)
print("안녕하세요"[1])   #녕
print("안녕하세요"[2])   #하
print("안녕하세요"[3])   #세
print("안녕하세요"[4])   #요
print("안녕하세요"[-1])  #요 (뒤에서부터 출력)
print("안녕하세요"[-2])  #세

#부분문자열
print("안녕하세요"[1:3]) #녕하    1번인덱스부터 2번인덱스까지 부분문자열 출력
print("안녕하세요"[:3])  #안녕하    0번인덱스부터 3번인덱스까지
print("안녕하세요"[3:])  #세요 3번인덱스부터 끝까지 부분문자열 출력
print("안녕하세요"[::2]) #안하요 앞부터 2칸 건너서 출력
print("안녕하세요"[::-1]) #요세하녕안 뒤부터 한자씩
print("안녕하세요"[::-2]) #요하안 뒤부터 2칸 건너서 출력

print(type("안녕하세요")) #str 타입확인
print("'안녕하세요' 문자열 길이 : ",len("안녕하세요"))
leng = len("안녕하세요")
print(type(leng))


a = "hello"
cnt = 0;
for i in range(0,len(a)) :
    if a[i]=="l" :
        cnt +=1
print("l 문자의 갯수=",cnt)
print("l 문자의 갯수=",a.count('l'))
print("l 문자의 위치=",a.find("l"))
print("a 문자의 위치=",a.find("a"))  #-1이 나오는데 없다는걸뜻한다.
print("l 문자의 위치=",a.index("l"))
print("az 문자의 위치=",a.index("a"))  #없으면 아예 에러로 빼준다.        