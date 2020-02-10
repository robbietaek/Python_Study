'''
Created on 2020. 2. 10.

@author: GDJ_19
'''
import yaml #pip install pyYAML
from test.test_quopri import QuopriTestCase

yaml_str = '''
    Date : 2019-01-03
    PriceList:
        -
            item_id : 1000
            name : nanana
            color : yellow
            price : 800
        -
            item_id: 1001
            name : orange
            color : orange
            price : 1400
        -
            item_id : 1002
            name : Apple
            color : red
            price : 2400

'''
data = yaml.load(yaml_str,Loader=yaml.FullLoader)
print(type(data))
print(data["Date"],"과일가격")
for item in data["PriceList"] : 
    print(item["name"],item["price"])
    
customer = [
        {"name":"Inseong", "age" : "24", "gender" : "man"},
        {"name":"kildong", "age" : "22", "gender" : "man"},
        {"name":"ChunHang", "age" : "20", "gender" : "woman"},
        {"name":"HangDan", "age" : "25", "gender" : "woman"},
    ]
#파이썬 데이터(List) 를 yaml 문서 양식으로 변경하기
yaml_str = yaml.dump(customer)
print(type(yaml_str))
print(yaml_str)

#yaml문서를 파이썬 자료형(List)로 변경
data = yaml.load(yaml_str,Loader=yaml.FullLoader)
for d in data :
    print(d["name"],d["age"],d["gender"])