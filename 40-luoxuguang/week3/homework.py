
# coding: utf-8


#1,打印出100以内的斐波那契数列，使用2种方法实现

i = 1
j = 2
n = i + j
print(i)
print(j)
while n < 100:  
    print(n)
    i = j
    j = n
    n = j + i
     


# In[53]:


def fei(n):
    if n <= 2:
        return n + 1
    else:
        return (fei(n-1) + fei(n-2))

for i in range(10):
    print(fei(i))


# In[62]:



# 2,使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上

for i in range(200):
    str = ''
    for j in range(5):        
        str += random.choice('abcdefghijklmnopqrstuvwxyz')
    print(str)




"""
(0 + 0)

    没有import random 模块，作业做完了，自己运行检测下代码
"""

