#!/usr/bin/env python
# coding: utf-8

# In[1]:


#打印出100以内的斐波那契数列，使用2种方法实现
a = 0 
b = 0 
for i in range(3):
    if i<=1:
        a = i
        num = (a+b)
        print(num)
else:
    print(num)
c = 0 
while c<=80:
    c = a+num
    a = num
    num = c
    print(c)


# In[2]:


##打印出100以内的斐波那契数列，使用2种方法实现
a = 0
b = 1
c = 0
print(a)
print(b)
while c < 100:
    c = a+b
    while c < 100 :
        print(c)
        temp = b
        a = temp
        b = c
        break
    


# In[3]:


#使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上
import random 
i = 1
while i < 200:
    i += 1
    a = ''.join(random.sample('0123456789',6))
    print(a)


# In[ ]:




