'''
Created on 2020. 1. 21.

@author: GDJ_19
'''
import sys
input_file = sys.argv[1]    #argv[0]은 시스템이다.    #jeju1.csv
output_file = sys.argv[2]   #jsju1_bak.csv
with open(input_file,'r',newline="") as filereader :
    with open(output_file, 'w', newline="") as filewriter :
        header = filereader.readline()
        header = header.strip()     #공백제거
        print(header)
        header_list = header.split(",") #,로 나눠서 리스트에 저장
        print(header_list)
        filewriter.write(",".join(map(str,header_list))+"\r\n")
        
        for row_list in filereader :    #문자열 형태로
            filewriter.write("".join(map(str,row_list)))
        
