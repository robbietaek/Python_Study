'''
Created on 2020. 1. 17.

@author: GDJ_19

classex3 : 상속 예쩨, 오버라이딩.
                다중상속 가능 => 자손클래스의 부모클래스가 여러개 가능
'''

class Car :
    speed = 0
    room = 3
    def upSpeed(self,value):
        self.speed+= value
        print("현재속도(부모클래스) : %d" % self.speed)
        
class Sedan(Car):       #상속표현
    pass                #추가되는 멤버가 없는 경우
       
        
class Truck(Car): #상속표현
    def upSpeed(self, value): #인스턴스 메서드는 self 가 된다.
        self.speed += value
        if self.speed >150 :
            self.speed =150
        print("현재 속도(자손 클래스) : %d" % self.speed)        
            
            
class Container : 
    room = 1
class MovingCar (Car,Container):
    pass

sedan1, truck1, mcar = None, None, None
truck1 = Truck()
sedan1 = Sedan()
mcar = MovingCar()

print("이동차량의 방개수 : ",mcar.room,",",end="")
mcar.upSpeed(60)


print("트럭 ->", end  ="")
truck1.upSpeed(200)

print("승용차->",end = "")
sedan1.upSpeed(200)
