'''
Created on 2020. 1. 10.

@author: GDJ_19
dictionaryex2.py : 딕셔너리 예제2
'''
foods = {"떡볶이":"오뎅","짜장면":"단무지","라면":"김치","맥주":"치킨"}
for i in foods.keys() :
    print("%s=>%s" % (i,foods[i]))
    
#화면에서 음식 하나를 입력받아서 해당하는 궁합음식을 출력하기

while True :
    myfood = input(str(list(foods.keys()))+"중에 음식 이름을 입력하세요 : ")
    if myfood=='종료' :
        print("총 "+str(len(foods))+"개 입니다.")
        print("좋아하는 음식 : "+str(list(foods.keys())))         #키값만가져오기
        print("궁합 음식 : "+str(list(foods.values())))         #value 값만 가져오기
        print(list(foods.items()))            #튜플 형태로 가져온다. 상수로 인식한다.
        print(list(foods.items())[-1])
        break
    if myfood in foods :
        print("<%s> 궁합음식은 <%s> 입니다." % (myfood,foods[myfood]))
    else :
        answer = str(input(myfood + "은(는) 등록된 음식이 아닙니다. 등록하시겠습니까? Y/N "))
        if answer == "Y" or answer == "y" :
            friend = input(myfood+"의 궁합 음식이름을 입력하세요 : ")
            foods[myfood] = friend
            print("등록이 완료되었습니다.")
