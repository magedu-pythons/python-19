#!/usr/bin/env python
lst = [1,1,2]
i=3
while True:
    tail=lst[i-1] + lst[i-2]
    if tail < 100:
        lst.append(lst[i-1] + lst[i-2])
        i+=1
    else:
        break

print(lst)

