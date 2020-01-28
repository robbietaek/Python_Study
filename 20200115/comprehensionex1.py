'''
Created on 2020. 1. 15.

@author: GDJ_19
'''
numbers = []
for n in range(1,11) :
    numbers.append(n)
print(numbers)

print([x for x in range(1,11)]) #이 방식이 comprehension 방식이다.

numlist = [x for x in range(1,11)]
print(numlist)

#1~10까지 짝수 리스트 생성
evenlist = []

for i in range(1,11) :
    if i%2 ==0 :
        evenlist.append(i)
print(evenlist)    

evenlist = [x for x in range(1,11) if x % 2 ==0]    #필터를 설정해줬다.
print(evenlist)

evenlist = [x for x in range(1,11) if x % 2 ==0 if x % 3 ==0]    #2의 배수이면서 3의 배수인것 조건문을 여러개로 쓸 수 도 있음.
print(evenlist)

#중첩사용 컴프리헨션
matrix = [[1,2,3],[4,5,6],[7,8,9]]
mlist = [x for row in matrix for x in row]  #중첩하여 사용가
print(mlist)

#set 컴프리헨션
set1 = {x**2 for x in [1,2,3]}      #set 이다. dictionary 도 키값이 중복될 수 없기 때문에 어떻게 보면 set이다.
print(set1)

#1부터 10까지의 수 중 짝수의 제곱을 출력하기 : 컴프리헨션 문법 이용하기
set2 = {x**2 for x in range(1,11) if x % 2 == 0}
print(sorted(set2))