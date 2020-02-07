'''
Created on 2020. 2. 3.

@author: GDJ-19
pandasexcelex3.py : 
    Purchase Date 컬럼중 값이 '01/24/2013'와 '01/31/2013'인
    행만 조회하여 pandas_output3.xls에 저장하기

'''
import pandas as pd
input_file = "sales_2013.xlsx"
output_file = "pandas_output3.xls"
# data_frame : sales_2013.xlsx 파일의 january_2013 sheet
#              모든 내용
data_frame = pd.read_excel\
                (input_file,"january_2013",index_col=None)
select_date = ['01/24/2013','01/31/2013']
# isin : select_date 속한 값인 경우만 선택
# data_frame_value : '01/24/2013','01/31/2013' 날짜에 해당하는 모든데이터
data_frame_value = \
                data_frame[data_frame['Purchase Date'].isin(select_date)]
writer = pd.ExcelWriter(output_file)
data_frame_value.to_excel\
(writer,sheet_name="jan_13_output",index=False)
writer.save() # 파일로 저장