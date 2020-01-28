'''
Created on 2020. 1. 10.

@author: GDJ_19
listex2.py : 리스트의 기본 함수
'''
mylist = [30,10,20]
print("리스트 : %s" % mylist)
mylist.append(40)
print("mylist.append(40) 후 리스트 : %s" % mylist)

print("pop() 메서드 결과 : %s" % mylist.pop())
print("mylist.pop() 메서드 후 리스트 : %s" % mylist)

mylist.sort()
print("mylist.sort() 후 리스트 : %s" % mylist)
mylist.reverse()
print("mylist.reverse() 후 리스트 : %s" % mylist)

print("20 값의 위치 : %d" % mylist.index(20))
mylist.insert(2,2222)
print("mylist.insert(2,2222) 후 리스트 : %s" % mylist)
mylist.remove(2222)
print("mylist.remove(2222) 후 리스트 : %s" % mylist)
mylist.extend([77,77,99])
print("mylist.extend([77,77,99]) 후 리스트 : %s" % mylist)
print("77값의 갯수 : %s" % mylist.count(77))