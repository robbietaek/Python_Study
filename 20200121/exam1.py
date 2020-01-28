'''
Created on 2020. 1. 21.

@author: GDJ_19
'''
import codecs

new_file = ""

filename = 'jeju1.csv'
csv = codecs.open(filename, "r", "euc-kr").read()
data = []
rows = csv.split("\r\n")
for row in rows : 
    if row == "" : continue
    cells = row.split(",")
    data.append(cells)
for c in data :
    new_file += ("%s %s %s \n" % (c[0],c[1],c[2]))
    
outfp = open("jeju2.txt","w",encoding='UTF8')
   
for i in range(1)   :
    outStr = new_file
    outfp.writelines(outStr)    

outfp.close()

    
    