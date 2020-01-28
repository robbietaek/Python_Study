'''
Created on 2020. 1. 9.

@author: GDJ_19
forex1.py : 구구단출력하기
'''

i,j = 0,0

for i in range(2,10) :
    print("%5d단" %i)
    for j in range(1,10) :
        print(i,"*",j,"=",i*j)
    print("")