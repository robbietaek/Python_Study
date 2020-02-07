'''
Created on 2020. 2. 4.

@author: GDJ-19
graph2.py : 그래프 여러개 작성하기
'''
# numpy : python에서 사용되는 리스트형태의 수치 처리 모듈
import numpy as np
import matplotlib.pyplot as plt # pip install ggplot

# 도화지 2행 2열로 나눠서 사용
# ax_lst : 그래프 리스트
# fig : 도화지
fig, ax_lst = plt.subplots(2,2,figsize=(8,5))
fig.suptitle('figure sample plots')
ax_lst[0][0].plot([1,2,3,4])
ax_lst[0][1].plot(np.random.randn(4,10),np.random.randn(4,10))
ax_lst[1][0].plot(np.linspace(0.0,5.0),
                  np.cos(2*np.pi*np.linspace(0.0,5.0)))
ax_lst[1][1].plot([3,7],[5,4])
plt.show()