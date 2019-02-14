#!/usr/local/python3/bin/python3
import random
l = []
for i in range(20):
    l.append(random.randrange(10))
#print(max(l))
for a in range(len(l) - 1):
    for aa in range(len(l)-a-1):
        if l[aa] > l[aa+1]:
            l[aa], l[aa+1] = l[aa+1],l[aa]
_,*_,b,c,d = l
print(b,c,d)
