'''
Created on 2020. 1. 21.

@author: GDJ_19
open (파일이름, 파일모드, [인코딩방식])

파일 모드
    "r" : 읽기모드
    "w" : 쓰기모드, 파일이 존재하지 않으면 생성
    "rt" : 읽기/쓰기 겸용
    "a" : 쓰기 모드. append 모드. 파일이 존재하지 않으면 생성
            존재하는 경우는 기존 내용 이후에 추가됨
    "t" : 텍스트 모드. 기본형
'''
infp = None
inStr = ""
infp = open("../20200120/regularex3.py","rt",encoding='UTF8')
while True : 
    inStr = infp.readline()
    if inStr == None :      #EOF (end of file) 상태
        break
    print(inStr,end="")
infp.close()