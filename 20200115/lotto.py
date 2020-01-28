'''
Created on 2020. 1. 15.

@author: GDJ_19
'''
import random
def getNum():
    return random.randrange(1,46)
lotto = set()
while len(lotto) < 7 :
    lotto.add(getNum())
    
print("추첨된 로또 번호 =>", sorted(lotto))