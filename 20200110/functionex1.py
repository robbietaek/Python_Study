'''
Created on 2020. 1. 10.

@author: GDJ_19
functionex1.py : 함수사용하기
'''
#함수선언
def coffee_machine(button) :
    print()
    print("#1 뜨거운 물 준비")
    print("#2 종이컵 준비")
    if button == 1 :
        print("#3 보통커피를 탄다")
    elif button == 2 :
        print("#3 설탕커피를 탄다")
    elif button == 3 :
        print("#3 블랙커피를 탄다")
    else :
        print("#3 커피 종류 없음")
    print("#4 물을 붓는다")
    
    
#main함수 시작    
coffee = int(input("커피 종류를 입력하세요(1:보통, 2:설탕, 3: 블랙)"))
coffee_machine(coffee)    