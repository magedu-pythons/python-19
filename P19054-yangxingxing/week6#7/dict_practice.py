import random
from asyncio import AbstractEventLoop
from collections import defaultdict
# 字典练习1, 打印每一位数字及其重复的次数。
num_str = input('Enter your num >: ').strip()
#repeat = {}
#for i in num_str:
#    if i not in repeat:
#        repeat[i] = 1
#    else:
#        repeat[i] += 1
#print(repeat)

# 计数这里有很多种写法:
# 1、
#repeat = defaultdict(int)
#for i in num_str:
#    repeat[i] += 1
# 2,
#repeat = {}
#for i in num_str:
#    repeat[i] = repeat.get(i, 0) + 1
#
#print(repeat)

# 字典练习2， 数字重复统计。 生序输出所有不用的数字及其重复的次数。
#repeat_dict = {}
#for _ in range(100):
#    n = random.randint(-1000, 1000)
#    if n in repeat_dict:
#        repeat_dict[n] += 1
#    else:
#        repeat_dict[n] = 1
#
#sort_list = list(repeat_dict)
#length = len(sort_list)
## 二元选择排序
#for i in range(length // 2):
#    max_index = i
#    min_index = i
#    for y in range(i+1, length-i):
#        if sort_list[y] > sort_list[max_index]:
#            max_index = y
#        elif sort_list[y] < sort_list[min_index]:
#            min_index = y
#    if min_index == max_index:
#        break
#    if i != max_index:
#        sort_list[i], sort_list[max_index] = sort_list[max_index], sort_list[i]
#        if min_index == i:
#            min_index = max_index
#    if length-i-1 != min_index:
#        sort_list[-i-1], sort_list[min_index] = sort_list[min_index], sort_list[-i-1]
#
#for index in sort_list:
#    print(index, repeat_dict[index])


# 字典练习3， 字符串重复统计。
#str_table = 'abcdefghijklmnopqrstuvwxyz'
#repeat_dict = {}
#for _ in range(100):
#    str = ''
#    for _ in range(2):
#        str += random.choice(str_table)
#    if str not in repeat_dict:
#        repeat_dict[str] = 1
#    else:
#        repeat_dict[str] += 1
#
#sort_list = list(repeat_dict)
#length = len(sort_list)
#for i in range(length-1):
#    for n in range(length-i-1):
#        if sort_list[n+1] > sort_list[n]:
#            sort_list[n], sort_list[n+1] = sort_list[n+1], sort_list[n]
#
#for index in sort_list:
#    print(index, repeat_dict[index])




