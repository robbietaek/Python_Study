'''
Created on 2020. 1. 14.

@author: GDJ_19
'''

before = ["2019","07","15"]
print(type(before[0]))
after = list(map(int,before))
print(type(after[0]))

num = int("100") + 1
print(num)

mylist = [1,2,3,4,5]
#map을 이용하여 mylist 각각의 값에 10을 더하기
add = lambda num:num+10
mylist = list(map(add,mylist))
print(mylist)

list1 = [1,2,3,4]
list2 = [10,20,30,40]

#haplist 리스트에 list1 과 list2의 각각이 더한 값을 저장하기
add = lambda num1=0,num2=0 :num1+num2
haplist = list(map(add,list1,list2))
print(haplist)