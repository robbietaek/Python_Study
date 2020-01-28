'''
Created on 2020. 1. 28.

@author: GDJ_19
excelex5.py : 
문제 : ssec1804.xls 파일에서 "1.남자","1.여자" sheet를 선택하여 남자, 여자 ssec1804mf.xls로 저장하기
'''
from xlrd import open_workbook
from xlwt import Workbook

def makesheet(output_sheet):
    for row_index in range(worksheet.nrows) : 
        for column_index in range(worksheet.ncols) :
            output_sheet.write(row_index, column_index, worksheet.cell_value(row_index, column_index))
            print(worksheet.cell_value(row_index, column_index))
            
input_file = "ssec1804.xls"
output_file = "ssec1804mf.xls"

output_workbook = Workbook()
output_sheet_male = output_workbook.add_sheet("남자")
output_sheet_female = output_workbook.add_sheet("여자")

with open_workbook(input_file) as workbook :
    worksheet = workbook.sheet_by_name("1.남자")
    makesheet(output_sheet_male)
    worksheet = workbook.sheet_by_name("1.여자")
    makesheet(output_sheet_female)

output_workbook.save(output_file)