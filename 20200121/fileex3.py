'''
Created on 2020. 1. 21.

@author: GDJ_19
'''
import os.path
file = 'C:\\Data\\Python\\nofile.txt'
file = "csvex1.py"
file = '../20200120'
if os.path.isfile(file):
    print("Yes. it is a file")
if os.path.isdir(file):
    print("Yes. it is a directory")
if os.path.exists(file) :
    print("Something exist")
else :
    print("Nothing")