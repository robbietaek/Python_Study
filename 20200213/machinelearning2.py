'''
Created on 2020. 2. 13.

@author: GDJ_19
'''
import pandas as pd
from sklearn import svm,metrics
xor_input = [[0,0,0],[0,1,1],[1,0,1],[1,1,0]]   #매트릭스 형태
xor_df = pd.DataFrame(xor_input)    #pandas 자료형 변환
xor_data = xor_df.loc[:,0:1]    #모든 열, 0~1행까지
xor_label = xor_df.loc[:,2] #정답
clf = svm.SVC() #사이킷런 객체. 머신러닝 툴
clf.fit(xor_data,xor_label) #학습하기
pre = clf.predict(xor_data) #평가실행, 답안지
ac_score = metrics.accuracy_score(xor_label,pre)    #정답지와 답안지를 비교를해서 정답률을  넣은 것
print("정답률=",ac_score)  #1이 100% 다 맞은 것
print("test 데이터로 평가하기")
test = [[0,0],[1,1],[1,0],[0,1],[1,0],[1,1]]    #다시 예제를 주는것
pre = clf.predict(test) #평가 실행
ans = [0,0,1,1,1,0]
ac_score = metrics.accuracy_score(ans,pre)  #결과를 다시 넣는다.
print("test 정답률=",ac_score) #오답률이 있을 수 는 있다.