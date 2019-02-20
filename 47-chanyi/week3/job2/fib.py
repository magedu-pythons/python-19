#!/usr/bin/env python

## 打印出100以内的斐波那契数列，使用2种方法实现

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


##
fir=1
sec=1
print(fir,sec,sep='\n')
while True:
    val = fir+sec
    if val < 100:
        fir = sec
        sec = val
        print(val)
    else:
        break



"""
(0 + 0)

    作业安装week-demo方式来命名
"""