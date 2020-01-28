'''
Created on 2020. 1. 9.

@author: GDJ_19

#파이썬의 특징
1. 변수 선언 필요 없음.
2. { } 블럭이 없음.
    if. 반복문 내부에서 블록표시가 없다. => 공백으로 블록을 표시
3. ''' ''' 여러줄 주석
    #     한줄 주석
'''

#sel 은 정수가 된다.
sel = int(input('입력 진수 결정(16/10/8/2) : '))
#num 은 문자열로 저장이된다.
num = input('값 입력 : ')


if sel == 16 :
    num10 = int(num,16) #문자로 저장된 num을 int 로 바꿔서 저장해라.
#블럭종료    
if sel == 10 :
    num10 = int(num,10)
if sel == 8 :
    num10 = int(num,8)    
if sel == 2 :
    num10 = int(num,2)
print(num10)
print(type(num))
num = num10 #에러가 발생하지 않음. 바로 num이 정수형으로 바뀜. 동적으로 이동하는 것.
print(type(num))

#10진수를 각 진법으로 출력
print('16진수 =>', hex(num10))
print('8진수 =>', oct(num10))
print('2진수 =>', bin(num10))