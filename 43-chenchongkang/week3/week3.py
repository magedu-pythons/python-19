# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 21:16:27 2019

@author: CCKGOD
"""

#print Fibonacci 
#method one
print('=========================')
a=0
b=1
Fi=0
print(a)
print(b)
while Fi<100:
    Fi=a+b
    a=b
    b=Fi
    if b>=100:
        break
    print(Fi)

print('=========================')

#method two

a=0
b=1
print(a)
print(b)
for i in range(0,50):
    Fi=a+b
    b=a^b
    a=a^b
    b=Fi
    if Fi<100:
        print(Fi)
        continue
    
print('=========================')


#随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上

import random as rd
char='AaBbCcDdEe0123456789'
ActCode=''
list=[]
i=0
while i<200:
    i+=1
    for j in range(1,17):
        rand=rd.choice(char)
        if j==4 or j==8 or j==12:
            ActCode+=rand
            ActCode+='-'
        else:
            ActCode+=rand
            
    if ActCode not in list:         #判断激活码是否重复
        list.append(ActCode)
        print('第%d个激活码:%s'%(i,ActCode)) 
    else:
        print('重复')
        i-=1
    
    
    ActCode=''
    
#print(list)
#print(len(list))



