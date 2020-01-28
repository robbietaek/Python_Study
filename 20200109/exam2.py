'''
Created on 2020. 1. 9.

@author: GDJ_19
'''

time =int(input("초를 입력하세요"))
left = 0;

hour = 0;
minute = 0;
sec = 0;

hour = time//3600
left = time%3600

minute = left//60
left = time%60

sec = left

print("시간:", hour, "\n분:", minute, "\n초:", sec)

