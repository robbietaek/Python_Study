'''
Created on 2020. 1. 20.

@author: GDJ_19
'''
import pymysql


conn = pymysql.connect(host = "localhost", port = 3306, user = "scott", passwd = "1234", db = "classdb", charset = "utf8")

try:
    cur = conn.cursor()                         # 구문을 가져오겠다.
    cur.execute("select * from item")           # 구문을 실행하겠다.
#     while True :
#         row = cur.fetchone()                    # 레코드 한 건만 가져온다.
#         if row == None :                        # 읽을 레코드가 없음
#             break
#         print(row)
        
    for row in cur.fetchall() :
        print(row[0],row[1],row[2])
finally :
    cur.close()
    conn.close()