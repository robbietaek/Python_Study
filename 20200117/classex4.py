'''
Created on 2020. 1. 17.

@author: GDJ_19
classex4.py 클래스에서 사용되는 메서드
'''
class Line : 
    length = 0
    #클래스 객체 생성시 호출되는 메서드
    def __init__(self,length):
        self.length = length
        print(self.length,"길이의 선이 생성되었습니다.")
    
    #소멸자. 객체 제거시 호출되는 메서드
    def __del__(self):
        print(self.length, "길이의 선이 제거되었습니다.")
    
    #자바의 toString같은 기능의 메서드. 객체를 출력시 호출되는 메서드
    def __repr__(self):
        return "선의 길이" + str(self.length)
    
    #객체의 더하기 연산자 사용시 호출되는 메서드
    def __add__(self,other):
        print("더하기 연산자가 호출되었습니다.")
        return self.length + other.length
    
    def __lt__(self,other):
        print("< 연산자 호출")
        return self.length < other.length
    
    def __gt__(self,other):
        print("> 연산자 호출")
        return self.length > other.length
    
    def __eq__(self,other):
        print(" == 연산자 호출")
        return self.length == other.length
myLine1 = Line(100) #객체화 , 생성자 호출
myLine2 = Line(200)
print(myLine1)
print(myLine2)

print("두 선의 길이  합 : ", myLine1 + myLine2)


#두 선 길이를 비교
if myLine1 < myLine2 : 
    print("myLine2 선이 더 깁니다.")
elif myLine1 == myLine2 :
    print("두 선의 길이가 같습니다.")
else : 
    print("myLine1 선이 더 깁니다.")        

#프로그램 종료 : 생성된 객체가 모두 소멸됨. 소멸자가 호출 됨    