'''
Created on 2020. 1. 21.

@author: GDJ_19
'''
outfp = None
outfp = open("data.txt","w",encoding='UTF8')
while True : 
    outStr = input("내용입력")
    if outStr != "" :
        outfp.writelines(outStr + "\n")
    else :
        break
outfp.close()
print("프로그램 종료")