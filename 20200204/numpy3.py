'''
Created on 2020. 2. 4.

@author: GDJ-19
numpy3.py : numpy 예제 : 배열 사본 생성, 재구조화 예제
'''
import numpy as np

#0부터 9까지 임의의 난수 10개를 배열로 저장
x = np.random.randint(10, size=10)
x_sub = x[:2]
print(x)
print(x_sub)
x_sub[0]=20 #사본 (x_sub)의 0번째 요소를 20으로 바꿈
print(x)
print(x_sub)

# 배열의 복사하기
x_cop = x.copy()
x_cop[0] = 100
print(x)
print(x_cop)

# 배열의 재편성 : 10개의 요소를 2차원배열(5행2열)로 재편성
x2 = x.reshape(5,2)
print(x2)

# 0부터 9까지의 임의의 수를 9개로 이루어진 배열 생성
# 9개의 배열을 3행 3열 배열로 재편성
# => 재편성 할 때, 요소의 갯수가 맞아야 함
arr = np.random.randint(10, size=9)
arr2 =arr.reshape(3,3) 
print(arr)
print(arr2)