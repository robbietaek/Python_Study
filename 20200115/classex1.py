'''
Created on 2020. 1. 15.

@author: GDJ_19
'''
#기본 생성자 : __init__ (self) : 구현된 생성자가 없는 경우 시스템이 제공하는 생성자가 기본 생성자이다.
class Car :
    color = ""
    speed = 0
    #생성자 추가하기
    
    def __init__(self,v1="",v2=""):
        self.color = v1
        self.speed = v2
        
    def upSpeed(self,value):    #메서드
        self.speed += value
    def downSpeed(self,value):  #메서드
        self.speed += value       
        
        
myCar1 = Car()   #객체화 (생성자를 default 로 설정해주면 아무것도 넣지 않아도 됨)
myCar1.color ="빨강"
myCar1.speed = 0
myCar1.upSpeed(30)
print("자동차1의 색상은 %s 이며, 현재 속도는 %dkm 입니다." % (myCar1.color,myCar1.speed))
myCar2 = Car("파랑",50)
myCar2.downSpeed(20)
print("자동차2의 색상은 %s 이며, 현재 속도는 %dkm 입니다." % (myCar2.color,myCar2.speed))