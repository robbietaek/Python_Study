'''
Created on 2020. 1. 9.

@author: GDJ_19
opex1.py : 연산자 연습
'''

num1 = int(input("첫번째 정수 입력 : "))
num2 = int(input("두번째 정수 입력 : "))
print(num1,"+",num2,"=",(num1+num2))
print(num1,"-",num2,"=",(num1-num2))
print(num1,"*",num2,"=",(num1*num2))
print(num1,"**",num2,"=",(num1**num2))    #제곱은 별두개
print(num1,"/",num2,"=",(num1/num2))    #소숫점 처리 알아서 해줌
print(num1,"//",num2,"=",(num1//num2))    #정수/정수는 정수값으로 가져와
print(num1,"%",num2,"=",(num1%num2))

print("a"+"b"+"c")  #abc 로 나옴
print("a","b","c")  #a b c 로 나옴
print("abc"*3)  #abcabcabc 나옴
print("""안녕하세요, 홍길동입니다. 반갑습니다. 어쩌구 저쩌구........
안녕하세요, 홍길동입니다. 반갑습니다. 어쩌구 저쩌구........""")