'''
Created on 2020. 2. 3.

@author: GDJ-19
pandasexcelex8.py : 폴더에 속한 excel 파일을 선택
'''
import pandas as pd
import glob # 경로명 표현시 사용되는 모듈
import os # 시스템 관련 모듈
input_path="C:/Users/GDJ-19/Python/python/excel/"
output_file = "pandas_output8.xlsx"
# input_path, "*.xls*" : input_path 폴더의 모든 xlsx 또는 xls 파일 모두
# all_workbooks : input_path폴더의 모든 excel파일을 저장
all_workbooks = glob.glob(os.path.join(input_path,"*.xls*"))
data_frames=[]
for workbook in all_workbooks :
    # workbook : 한개의 엑셀 파일을 저장
    all_worksheets = pd.read_excel(workbook,sheet_name=None,index_col=None)
    for worksheet_name, data in all_worksheets.items() :
        data_frames.append(data)
# all_data_concat : 모든 엑셀 파일의 data를 저장
all_data_concat = pd.concat(data_frames,axis=0,ignore_index=True)
writer = pd.ExcelWriter(output_file)
all_data_concat.to_excel(writer,sheet_name="all_data_all_worksheet",index=False)
writer.save()