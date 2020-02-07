'''
Created on 2020. 2. 7.

@author: GDJ_19
배열의 연결 및 분할
'''
import numpy as np
#같은 차원의 배열 연결
x = np.array([[1,2,3],[4,5,6]])
y = np.array([[3,2,1],[6,5,4]])

print(x)
print(y)
print(np.concatenate([x,y], axis = 0))  #수직연결
print(np.concatenate([x,y], axis = 1))  #수평연결

#혼합된 차원의 배열 연결
x = np.array([[1,2,3],[4,5,6]])
y = np.array([[3,2,1],[6,5,4],[3,2,1]])
z = np.array([[7],[10]])
print(np.vstack([x,y])) #x와 y의 수직스택
print(np.hstack([x,z])) #x와 y의 수평스택
#print(np.vstack([x,z])) #오류발생 (열 길이가 다름)
#print(np.vstack([y,z])) #오류발생 (행 길이가 다름)

#배열의 분리
# 0 ~ 15 까지 값을 가진 배열을 4행 4열로 배치
x = np.arange(16).reshape((4,4))
print(x)
upper, lower = np.vsplit(x,[2]) #2행을 기준으로 자름
print(upper)
print(lower)
left, right = np.hsplit(x,[2]) #2열을 기준으로 자름
print(left)
print(right)

 

