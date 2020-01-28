'''
Created on 2020. 1. 28.

@author: GDJ_19
excel 파일을 pandas 로 읽기
'''

import pandas as pd

input_file = "sales_2015.xlsx"
output_file = "pandas_output.xls"
data_frame = pd.read_excel(input_file,"january_2015",index_col=None)
data_frame_value = data_frame[data_frame['Sale Amount'].astype(float)>300.0]    #컬럼의 이름이 Sale Amount 를 가져오고 300 이상만 가져와.
#data_frame_value 조건에 맞는 데이터 저장
writer = pd.ExcelWriter(output_file)
data_frame_value.to_excel(writer,sheet_name="jan_15_output",index = False)

writer.save()       #파일로 생성