'''
Created on 2020. 2. 10.

@author: GDJ_19
'''
import json
savename = "fruits.json"
price = {
    "date" : "2020-02-10",
    "price" : {
        "Apple" : 800,
        "Orange" : 1000,
        "Banana" : 500
        }
    }

print("날짜",price["date"])
for p in price["price"].keys() :
    print("%s = > %s" % (p,price["price"][p]))
s = json.dump(price, open("json_output2.json","w"))    
