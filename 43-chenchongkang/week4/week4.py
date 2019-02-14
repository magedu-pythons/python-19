# -*- coding: utf-8 -*-



 #1、给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0

import random as rd
char='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
Inp=input('Please input a letter：')
lst0=[]
for i in range(20):
    rand=rd.choice(char)
    lst0.append(rand)
print(lst0)

if Inp in lst0:
    print(1)
else:
    print(0)



print('=========================')


# 2、任一个英文的纯文本文件，统计其中的单词出现的个数。
lst=[]
for line in open("C:\\Users\\CCKGOD\\Documents\\GitHub\\python-19\\43-chenchongkang\\week4\\test.txt"):
    l=len(line.split())
    lst.append(l)
print(lst)
words=sum(lst)
print(words)





"""
(0 + 0)

    题二请参考答案实现
"""

