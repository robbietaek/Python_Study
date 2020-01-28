'''
Created on 2020. 1. 10.

@author: GDJ_19
'''
def calc(v1,v2,op):
    print("res=",res)
    result = 0
    if op == '+' :
        result = v1 + v2
    elif op =='-' :
        result = v1 - v2
    elif op =='*' :
        result = v1 * v2
    elif op =='/' :
        result = v1 / v2
    return result
        
#전역변수 선언부분        
res = 10
var1,var2,oper = 0,0,""

#main 함수
oper = input("수식을 입력하세요 (+,-,*,/) :")
var1 = int(input("첫번째 수 :"))
var2 = int(input("두번째 수 :"))
res = calc(var1,var2,oper)
print("계산 : %d %s %d = %d" % (var1,oper,var2,res))                        
