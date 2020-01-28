'''
Created on 2020. 1. 10.

@author: GDJ_19
 python : list(배열) => [],
          dictionary(자바의 Map) => {}
          tuple(상수처리된 List) => () 
'''

a=[0,0,0,0]
b=[]
suma,sumb = 0,0
for i in range(0,len(a)) :
    a[i] = int(input(str(i+1)+"번째 값 :"))        #수정
    suma += a[i]
    b.append(a[i])  #추가
    sumb += b[i]
print(a)
print(b,len(b))    
print("a 리스트 합계 : ",suma)
print("b 리스트 합계 : ",sumb)
    