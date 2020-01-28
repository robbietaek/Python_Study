'''
Created on 2020. 1. 28.

@author: GDJ_19
'''
import openpyxl
filename = "sales_2015.xlsx"
book = openpyxl.load_workbook(filename)
for sheet in book.worksheets:
    data = []
    for row in sheet.rows :
        line = []
        for l, d in enumerate(row):
            line.append(d.value)    #한줄의 셀의 값들을 list로 저장
                #print(l,end="\t")
            print(line)
            data.append(line)
    print(data)
#enumerate : 리스트에서 데이터와 index 값을 제공
    for i, a in enumerate(data) :
        if(i>=10) :
            break;
        print(i+1,a)
