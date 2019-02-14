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
# 2.1
for num in range(1,100000):
    middle_num = num // 2
    for i in range(2,middle_num+1):
        if num % i == 0:
            break
    else:
        print(num, 'is prime number')


# 2.2,   开平方， 并且去掉2以外的偶数.
for num in range(1,100000):
    middle_num = int((num ** 0.5) + 1)
    if num % 2 == 0 and num != 2:
        continue
    for i in range(3,middle_num+1,2):
        if num % i == 0:
            break
    else:
        print(num)



