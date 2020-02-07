'''
Created on 2020. 2. 3.

@author: GDJ-19
pandasexcelex4.py : 열을 선택하기 
'''
import pandas as pd
input_file = "sales_2013.xlsx"
output_file = "pandas_output4.xls"
data_frame = pd.read_excel\
                (input_file,"january_2013",index_col=None)
data_frame_value=data_frame.loc\
                [:,["Customer Name","Purchase Date"]]
writer = pd.ExcelWriter(output_file)
data_frame_value.to_excel\
(writer,sheet_name="jan_13_output",index=False)
writer.save()
