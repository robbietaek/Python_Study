'''
Created on 2020. 1. 9.

@author: GDJ_19
'''

score = int(input("점수를 입력하세요"))
if score >= 90 :
    print("A학점")
else : 
    if score >= 80 :
        print('B학점')
    else :
        if score >= 70 :
            print("C 학점")
        else :
            if score >= 60 :
                print("D학점")
            else :
                print("F학점")
                
print('if elif 구문연습')
if score >= 90 :
    print("A학점")
elif score>= 80 :
    print("B학점")
elif score>= 70 :
    print("C학점")  
elif score>= 60 :
    print("D학점")  
else :
    print("F학점")                             