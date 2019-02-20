#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0
import random
seq = 'a b c d e f g h j k l q w e r t y u i o p z x v b n m'.split()
lst = []
for i in range(8):
    lst += random.choices(seq)
print(lst)
if 'a' in lst :
    print(1)
else:
    print(0)


# In[ ]:


#任一个英文的纯文本文件，统计其中的单词出现的个数
x = 'The very success of Beccaria’s work has so accustomed us to its result that we are apt to regard it, as men regard a splendid cathedral in their native town, with very little recognition of its claims to admiration. The work is there, they see it, they live under its shadow; they are even ready to boast of it; but[30] what to them is the toil and risk of its builders, or the care and thought of its architects? It may be said that this indifference is the very consummation Beccaria would most have desired, as it is the most signal proof of the success of his labour. So signal, indeed, has been that success, that already the atrocities which men in those days accepted as among the unalterable conditions of their existence, or resigned themselves to as the necessary safeguards of society, have become so repulsive to the world’s memory, that men have agreed to hide them from their historical consciousness by seldom reading, writing, or speaking of their existence. And this is surely a fact to be remembered with hopefulness, when we hear an evil like war with all its attendant atrocities, defended nowadays by precisely the same arguments which little more than a hundred years ago were urged on behalf of torture, but which have proved nevertheless insufficient to keep it in existence.'.split()
x.count('very')




"""
(0 + 0)

    使用函数封装，参考答案实现
"""