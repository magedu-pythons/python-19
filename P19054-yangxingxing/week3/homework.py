#!/usr/bin/env python
#

# 1、打印100以内裴波那契数列
# 第一种 
x = y = 1
while y < 100:
    print(x)
    z = x + y
    x = y
    y = z
# 第二种
x = y = 1
while True:
    if x >= 100:
        break
    print(x)
    z = x + y
    x = y
    y = z
    
# 第三种
n = [1,1]
while n[0] < 100:
    n.append(n[0] + n[1])
    print(n.pop(0))
    
     
# 2、200个优惠吗
# 第一种
len_code = 8
for i in range(200):
    if i > 99:
        len_num = 3
    elif i > 9:
        len_num = 2
    else:
        len_num = 1
    str_code = str(i) + 'a' * (len_code - len_num)
    print(str_code)

# 第二种
len_code = 8
for i in range(200):
    str_code = str(i)
    len_num = len(str_code)
    str_code = str_code + 'a' * (len_code - len_num)
    print(str_code)




