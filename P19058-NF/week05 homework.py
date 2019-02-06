#!/usr/bin/env python
# coding: utf-8

# In[9]:


a = input('>>>')
length = len(a)
flag = False
for i in range(length//2):
    if a[i] == a[-i-1]:
        continue
    else:
        flag = True
if not flag:
    print('palindrome number')
else:
    print('not palindrome number')
    


# In[15]:


import random
s = {random.randint(0,100) for _ in range(20)}
max_s = sorted(s,reverse=True)
print(max_s)
print(max_s[0],max_s[1],max_s[2])

