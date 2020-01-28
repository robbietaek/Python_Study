'''
Created on 2020. 1. 17.

@author: GDJ_19
'''
class SuperClass : 
    def method(self):
        raise NotImplementedError   #반드시 오버라이딩 해야함 구현하지 않으면 에러임. 추상메서드
    
class SubClass1(SuperClass):
        def method(self):
            print("SubClass1에서 method()를 오버라이딩함")
            
class SubClass2(SuperClass):
        def method(self):
            print("SubClass2에서 method()를 오버라이딩함")

sub1 = SubClass1()
sub2 = SubClass2()

sub1.method()
sub2.method()