'''
Created on 2020. 2. 3.

@author: GDJ-19
pandasexcelex6.py : 모든 sheet들의 열을 선택하기
'''
import pandas as pd
input_file = "sales_2013.xlsx"
output_file = "pandas_output6.xls"
data_frame = pd.read_excel(input_file,sheet_name=None,index_col=None)
column_output=[]
# data_frame.items() : sheet전체
# worksheet_name : sheet 이름
# data : sheet에 해당하는 데이터
for worksheet_name, data in data_frame.items():
    column_output.append(data.loc[:,["Customer Name","Sale Amount"]])
# axis = 0 : row를 추가
# axis = 1 : column를 추가
select_cols = pd.concat(column_output,axis=1,ignore_index=True)
writer = pd.ExcelWriter(output_file)
select_cols.to_excel(writer,sheet_name="select_column_all",index=False)
writer.save()
