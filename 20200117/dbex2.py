'''
Created on 2020. 1. 17.

@author: gdj-19
dbex2.py : 화면에서 내용을 입력 받아, sqlite db에 내용 저장하기
'''
import sqlite3

dbpath = "test.sqlite"
con  = sqlite3.connect(dbpath)
cur = con.cursor()   # sql 구문을 전달하는 객체
cur.executescript('''
    drop table if exists usertable;
    create table usertable (id varchar(15) primary key,
        name varchar(20),
        email varchar(30),
        birthyear integer);
''')

while True :

    data1 = input("사용자 ID => ")
    if data1 == '' :
        break
    data2 = input("사용자 이름 => ")
    data3 = input("이메일 => ")
    data4 = input("출생년도 => ")
    sql = "insert into usertable values ('"  \
           + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
    cur.execute(sql)
    con.commit()
    
# 등록된 내용으로 select로 조회하기
cur = con.cursor()
cur.execute("select * from usertable")
list = cur.fetchall()
for row in list :
    print(row)
con.close()
    