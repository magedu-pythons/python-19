#!/usr/local/python3/bin/python3
import random
alist = [1,2,3,4,5]
def test():
    for i in range(10): 
        r1 = random.randint(0, 4) 
        r2 = random.randint(0, 4) 
        alist[r1],alist[r2] = alist[r2],alist[r1] 
    print(alist) 
#test()
