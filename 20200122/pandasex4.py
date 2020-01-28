'''
Created on 2020. 1. 22.

@author: GDJ_19
'''
import pandas as pd
input_file = "supplier_data.csv"
output_file = "pandas_out3.csv"
df = pd.read_csv(input_file)
df_col = df.iloc[:,[0,3]]       #0번 열과 3번열 조회
print("=======df.iloc[:,[0,3]] ====")
print(df_col)
df_col = df.iloc[0:4,0:3]       #0부터 4행, 0행부터 3행
print("=======df.iloc[0:4,0:3] ====")
print(df_col)
#모든 행의 Invoice Number, Cost 컬럼 조회
df_in_set = df.loc[:,["Invoice Number","Cost"]]      #  : 는 모든행
df_in_set = df.loc[df["Invoice Number"].str.startswith("920-"),["Invoice Number","Cost"] ]  #invoicd 에서 920 으로 시작하는
print(df_in_set)

df_col.to_csv(output_file, index = False)
