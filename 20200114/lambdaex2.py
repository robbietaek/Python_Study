'''
Created on 2020. 1. 14.

@author: GDJ_19
'''

myList=[1,2,3,4,5]

def add10(num):
    return num+10

for i in range(len(myList)) :
    myList[i] = add10(myList[i])
print(myList)


add = lambda num:num+10
for i in range(len(myList)) :
    myList[i] = add(myList[i])
print(myList)
