#打印出100以内的斐波那契数列，使用2种方法实现
#答案：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
#1
a = 1
b = 1
print(a)
print(b)
while True:
    c = a+b
    if c > 100:
        break
    a = b
    b = c
    print(c)
#2
list =[]
for i in range(11):
    if i ==0 or i ==1:#第1,2项 都为1
        list.append(1)
    else:
        list.append(list[i-2]+list[i-1])#从第3项开始每项值为前两项值之和
print(list)

#使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上
import random

for i in range(200):
    o = ''
    for y in range(10):
        o += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    print(o)