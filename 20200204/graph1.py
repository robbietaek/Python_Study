'''
Created on 2020. 2. 4.

@author: GDJ-19

graph1.py : 그래프 그리기
'''

import matplotlib.pyplot as plt # pip install ggplot

plt.style.use("ggplot")
customers=["JAVA","JSP","SRPING","HADOOP","PYTHON"] #리스트
print(range(len(customers)))
customers_index = range(len(customers)) # 0~4지 인덱스
print(type(customers_index)) # 5
sale_amounts = [65,90,85,60,95] # 데이터 리스트 설정

fig = plt.figure() # 그래프 저장 공간. 그래프를 그리기 위한 공간=도화지
ax1 = fig.add_subplot(1,1,1) # 1행 1열 1번째 그래프
#막대 그래프 그리기
ax1.bar(customers_index,sale_amounts,align="center",
       color="darkblue")
ax1.xaxis.set_ticks_position("bottom") # x축 설정
ax1.yaxis.set_ticks_position("left") # y축 설정
# x축 표시 설정
plt.xticks(customers_index,customers,rotation=0,fontsize="small")
plt.xlabel("Subject")
plt.ylabel("Score")
plt.title("Class Score")
# 이미지 저장하기
plt.savefig("bar_plot.png",dpi=400,bbox_inches="tight")
# 화면에 이미지 출력하기
plt.show()