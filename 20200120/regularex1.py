'''
Created on 2020. 1. 20.

@author: GDJ_19
정규식 예제 1, 정규화 모듈 사용 안함
'''

data = '''
    park 800905-1234567
    kim 700905-1234567
    choi 850114-a123456
'''

result = []
for line in data.split("\n") :
    word_result = []
    for word in line.split(" ") :
#word : park
#word : 800905-1234567       
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))    