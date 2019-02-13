#!/usr/bin/env python
#


# 1、查看x元素是否存在于列表
some = [1, 3, 45, 6, 7, 8, 'dkfjdklfd']
if 45 in some:
    print(1)
else:
    print(0)



# 2、统计英文的纯文本文件中单词出现的个数。
content = 'Hello World,This is a dog'
word = content.replace(',', ' ')
word_num = len(word.split())
