'''
Created on 2020. 2. 13.

@author: GDJ_19
https://github.com/pandas-dev/pandas/blob/master/pandas/tests/data/iris.csv
'''

from sklearn import svm, metrics
import random, re    #난수발생모듈, 정규화관련 모듈

csv = []
with open("iris.csv","r",encoding="utf-8") as fp :
    for line in fp :
        line = line.strip() #공백을 제거
        cols = line.split(",")  #, 로 구분하기, 단어구분
        # [0-9\.] : 0부터 9까지 숫자 또는 .
        # ^ : 시작문자
        # $ : 종료문자
        # + : 1개 이상
        # r'^[0-9\.]+$' : row 데이터 숫자나 . 으로 이루어져 있음
        #                =>float(n) 실수로 변경
        fn = lambda n:float(n) if re.match(r'^[0-9\.]+$',n) else n
        cols = list(map(fn,cols))   #실수로 변경됨
        csv.append(cols)    #iris.csv 파일을 자료형에 맞도록 저장
del csv[0]  #Header 부분 삭제. 첫줄이 실수가 아니다. 지워버리는 것
#csv 리스트 : data 만 저장됨.
random.shuffle(csv) #csv 데이터 섞기

total_len = len(csv)    #데이터 갯수
train_len = int(total_len * 2/3)    #학습 데이터 갯수
train_data = [] #학습데이터
train_label = []    #학습데이터의 정답
test_data = []  #테스트데이터
test_label = [] #테스트 데이터의 정답

for i in range(total_len) :
    data = csv[i][0:4]  #학습데이터
    label = csv[i][4]   #결과
    if i < train_len :
        train_data.append(data) #학습데이터로 저장
        train_label.append(label)   #학습데이터의 결과로 저장
    else : 
        test_data.append(data)  #학습 완료 후 평가 데이터로 저장
        test_label.append(label)    #학습 완료 후 평가 저장데이터로 저장
clf = svm.SVC()
clf.fit(train_data,train_label) #학습 하기
pre = clf.predict(test_data)    #test 하기
#정확도 결과 출력
ac_score = metrics.accuracy_score(test_label,pre)
print("정답률=" , ac_score)