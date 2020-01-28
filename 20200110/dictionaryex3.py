'''
Created on 2020. 1. 10.

@author: GDJ_19
dictionaryex3.py : 딕서녀리 예제3
'''
import operator

dic, list = {},[]
dic = {"Thomas":"토마스","Edward":"에드워드","Henry":"헨리", "Gothen":"고든","James":"제임스"}
list = sorted(dic.items(), key = operator.itemgetter(0),reverse = True) #첫번째 키 기준으로 역정렬
print(list) 
list = sorted(dic.items(), key = operator.itemgetter(1))    #한글기준정렬
print(list)
