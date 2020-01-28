'''
Created on 2020. 1. 21.

@author: GDJ_19
'''
import codecs
filename = 'jeju1.csv'
csv = codecs.open(filename, "r", "euc-kr").read()
data = []
rows = csv.split("\r\n")
for row in rows : 
    if row == "" : continue
    cells = row.split(",")
    data.append(cells)
for c in data :
    print(c[0],c[1],c[2])
    
    
    
    
    