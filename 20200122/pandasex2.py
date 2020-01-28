'''
Created on 2020. 1. 22.

@author: GDJ_19
'''
import pandas as pd

input_file = "supplier_data.csv"
output_file = "pandas_out1.csv"

data_frame = pd.read_csv(input_file)
print(type(data_frame))
important_dates = ["1/20/14","1/30/14"]

'''
data_frame_in_set : Purchase Date 열의 값이
                    "1/20/14", "1/30/14" 값에 속한 모든 컬럼 조회
'''
data_frame_in_set = data_frame.loc[data_frame["Purchase Date"].isin(important_dates), :]    #isin == 속해있는
#data_frame_in_set.to_csv(output_file, index = False)            #이 데이터를 csv로 만들어라
print(data_frame_in_set)