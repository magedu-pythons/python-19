#!/usr/bin/env python
## 任一个英文的纯文本文件，统计其中的单词出现的个数

sum = 0
with open("sample.txt") as f1:
    for i in f1:
        lst = i.split()
        for j in lst:
            if j.isalpha:
                pass
            else:
                lst.remove(j)
        sum += len(lst)

print(sum)
