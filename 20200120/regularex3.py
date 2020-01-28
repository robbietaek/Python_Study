'''
Created on 2020. 1. 20.

@author: GDJ_19
정규식 예제 3
'''

import re

string = "The quick brown fox jumps over the lazy dog,"
string_list = string.split()
pattern = re.compile("Th+e")
count = 0
for word in string_list :
    if pattern.search(word) : 
        count += 1
print("output #1 : {1:s}:{0:d} ".format(count,"개수"))

pattern = re.compile("(?P<match_word>The)",re.I)        #re.I = 대소문자 무시
print("output #2 :")
for word in string_list:
    if pattern.search(word) :
        print("{0}".format(pattern.search(word).group("match_word")))
        
string_to_find = r"The"     #r = row data
pattern = re.compile(string_to_find, re.I)
print("output #3 : {0}".format(pattern.sub("a",string)))    #The, the 문자열을 a 문자열로 치환
