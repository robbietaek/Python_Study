'''
Created on 2020. 2. 3.

@author: GDJ-19
pandasexcelex5.py : 모든 sheet 조회하기
'''

import pandas as pd
input_file = "sales_2013.xlsx"
output_file = "pandas_output5.xls"
# data_frame : 모든 sheet 정보를 저장
data_frame = pd.read_excel(input_file,sheet_name=None,index_col=None)
row_output = []
# data_frame.itmes() : 모든 sheet를 선택
for worksheet_name,data in data_frame.items() :
    # data : sheet 내용 저장
    print("==============",worksheet_name,"=============")
    row_output.append(data[data['Sale Amount'].
                           replace('$','').replace(',','').astype(float) > 2000.0])

#  for 구문 종료    
filtered_row = pd.concat\
                    (row_output,axis=0,ignore_index=True)
# axis=0 : row로 추가
# axis=1 : column로 추가
writer = pd.ExcelWriter(output_file)
filtered_row.to_excel\
                (writer,sheet_name="sale_amount_gt2000",index=False)
writer.save()
