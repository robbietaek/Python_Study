'''
Created on 2020. 1. 10.

@author: GDJ_19
exam3.py : 배열의 값의 합과 평균을 구하는 함수 작성하기
'''

def getSum(list):
    return sum(list)

def getMean(list):
    return sum(list)/len(list) if len(list) >0 else 0   #한줄로써야됨.. len(list)가 0보다 크면 앞에 식 실행하고 아니면 0 리턴
#    return sum(list)/len(list) \          '\' = 원래 한줄로 써야하는데 두줄로 쓸게 
#        if len(list) >0 else 0
    

list = [2,3,3,4,4,5,5,6,6,8,8]
print("list의 값의 합",getSum(list))
print("list의 값의 평균",getMean(list))

list2 = []
print("list의 값의 합",getSum(list2))
print("list의 값의 평균",getMean(list2))

tp = (2,3,3,4,4,5,5,6,6,8,8)    #튜플
print("tp의 값의 합",getSum(tp))
print("tp의 값의 평균",getMean(tp))