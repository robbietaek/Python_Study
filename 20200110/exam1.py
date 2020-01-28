'''
Created on 2020. 1. 10.

@author: GDJ_19
exam1.py : 리스트 문제
    aa,bb 배열을 생성하고
    aa 배열은 0부터 짝수 100개를 저장하고
    bb 배열은 aa배열의 역순으로 값을 저장하기.
    aa[0] ~ aa[9], b[99]~b[90] 값을 출력하기
'''

aa,bb = [],[]
num = 0
while True :
    if len(aa) == 100 :
        bb = aa[::-1]
        break
    
    aa.append(num)
    num += 2

for i in range(0,10) :
    print("aa[%2d]=%3d" % (i,aa[i]), end = ",")

print()

for i in range(99,89,-1) :
    print("bb[%2d]=%3d" % (i,bb[i]), end = ",")

    