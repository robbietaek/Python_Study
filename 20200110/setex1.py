'''
Created on 2020. 1. 10.

@author: GDJ_19
set(집합 클래스) 예제 => {}
'''
set1 = {1,2,3,4,5}
print(set1)
set2 = {1,2,3,1,4,2,3,3,5,3,2,1}
print(set2)
set3 = {5,6,7,8}
print(set3)


#교집합 
print("set1과 set3의 교집합",set1 & set3)
print("set1과 set3의 교집합 ",set1.intersection(set3))

#합집합
print("set1과 set3의 합집합",set1 | set3)
print("set1과 set3의 합집합 ",set1.union(set3))