'''
Created on 2020. 1. 22.

@author: GDJ_19
'''

import pandas as pd
df = pd.DataFrame({"A":[1,4,7], "B":[2,5,8], "C":[3,6,9]})
print(type(df))
print(df)
print(df.iloc[0])
print(df.iloc[1])

print(df.loc[0])    #행
print(df["A"])      #열



df = pd.DataFrame(data = [[1,2,3],[4,5,6],[7,8,9]], index = [2,"A",4],columns = [51,52,54])

print(df)
print("df.iloc[2]=>")
print(df.iloc[2])           #무조건 인덱스 기준. 순번. 순서 기준
print("df.loc[2]=>")
print(df.loc[2])            #인덱스 이름 기준

'''
행 선택 : iloc : 순서 기준
        loc : 이름 기준
열 선택 : df["A"] :
'''

