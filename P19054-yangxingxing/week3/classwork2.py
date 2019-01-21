#!/usr/bin/env python
#

# 1、求斐波那契数列第101项
count = 0 
x = y = 1
while True:
    z = x + y
    x = y
    y = z
    count += 1
    if count >= 101:
        break
print(x)


# 2、求10万内的所有素数
for num in range(1,100000):
    middle_num = num // 2
    for i in range(2,middle_num+1):
        if num % i == 0:
            break
    else:
        print(num, 'is prime number')
