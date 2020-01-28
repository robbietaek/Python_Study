'''
Created on 2020. 1. 13.

@author: GDJ_19
1.영어단어,한글의미를 가지고 있는 사전을 등록하는 프로그램을 작성하기
2. 사전을 작성하기 위한 메뉴 
   1:조회, 2:등록, 3:수정, 4:삭제, 9:종료
   위의 번호를 제외한 값을 입력받지 않는다.
2. 등록된 사전내용이 없는 경우 조회 메뉴는 선택할 수 없다.
3. 조회시 조건
   - 정렬방식을 지정할 수 있다. 영어기준, 한글 기준, 입력기준
   - 결과 참조
4. 등록시 조건
   - 같은 영어 단어가 입력되는 경우에는  이미 등록된 단어라 출력한다
   - 등록되지 않은 영어 단어인 경우 한글 의미를 입력받아
     사전에 등록한다.
5. 수정시 조건
    - 등록되지 않은 단어인 경우 등록되지 않은 단어라 출력한다.
    - 등록된 단어인 경우 한글 의미를 입력받아 수정한다.
 6. 삭제시 조건  
    - 등록되지 않은 단어인 경우 등록되지 않은 단어라 출력한다.
    - 등록된 단어인 경우 사전에서 제거한다.
7. 결과를 정답란에 입력하고, 파이썬소스를 첨부하기
'''
import operator

dic = {}
dictolist =[]
dictodic = {}

while True :
    if len(dic) == 0 :
        num = int(input("2:등록, 3:수정, 4:삭제, 9:종료 \n번호를 입력하세요.=>"))
                
        if num == 2 :
            en = input("등록할 영어 단어 =>")
            ko = input("등록할 한글 단어 =>")
            dic[en] = ko
        elif num == 3 :
            en = input("수정할 영어 단어 =>")
            if dic.__contains__(en) == True :
                ko = input("수정할 한글 단어 =>")
                dic[en] = ko
            else :
                print("등록된 단어가 아닙니다..")
        
        elif num == 4 :
            en = input("삭제할 영어 단어 =>")
            if dic.__contains__(en) == True :
                dic.pop(en)
            else :
                print("등록된 단어가 아닙니다..")
        
        elif num == 9 :
            print("종료합니다.")
            break;
        
        else :
            print("번호가 틀립니다.")
        
    elif len(dic) != 0 :
        num = int(input("1:조회, 2:등록, 3:수정, 4:삭제, 9:종료 \n번호를 입력하세요.=>"))
        
        if num == 1 :
            print("=========================등록된 단어 갯수 :",len(dic))
            arraylist = int(input("정렬기준(1:영문기준,2:한글기준 ,그외값 입력순서)=>"))
            if arraylist == 1 :
                dictolist = sorted(dic.items(), key = operator.itemgetter(0))
                for i in range(0,len(dictolist)) :
                    print("%s=%s" % (dictolist[i][0],dictolist[i][1]))
            elif arraylist == 2 :
                dictolist = sorted(dic.items(), key = operator.itemgetter(1))
                for i in range(0,len(dictolist)) :
                    print("%s=%s" % (dictolist[i][0],dictolist[i][1]))
            
            else :
                dictodic = dic
                for i in dictodic.keys() :
                    print("%s=%s" % (i,dictodic[i]))

        elif num == 2 :
            en = input("등록할 영어 단어 =>")
            if dic.__contains__(en) == False :
                ko = input("등록할 한글 단어 =>")
                dic[en] = ko
            else :
                print("이미 등록된 단어입니다.")
        elif num == 3 :
            en = input("수정할 영어 단어 =>")
            if dic.__contains__(en) == True :
                ko = input("수정할 한글 단어 =>")
                dic[en] = ko
            else :
                print("등록된 단어가 아닙니다..")
        
        elif num == 4 :
            en = input("삭제할 영어 단어 =>")
            if dic.__contains__(en) == True :
                dic.pop(en)
            else :
                print("등록된 단어가 아닙니다..")        
                
        elif num == 9 :
            print("종료합니다.")
            break;
        
        else :
            print("번호가 틀립니다.")
















