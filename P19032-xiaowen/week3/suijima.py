#!/usr/local/python3/bin/python3
import random

n = int(input("enter number: ")) #这里控制随机码长度
lst = []

#这里ascii码的转换
for i in range(65,91):
    lst.append(str(chr(i)))

for ii in range(97,123):
    lst.append(str(chr(ii)))

for iii in range(10):
    lst.append(str(iii))

#先给一个200长度的列表空间
ma = [1]*200

#生成200个随机码
for b in range(200):
    string = ""
    for a in range(n):
        c = random.choice(lst) #从字符列表中随机取一个
        string = string + c
    ma[b] = string  #索引替换
print(ma)



"""
(0 + 0)

    没有考虑重复生成的优惠码
"""