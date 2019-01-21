#2.打印100以内的裴波那契数列，使用2种方法实现
#第一种
import random
a=1
b=1
while b<100:
    a,b = b,a+b
    print(a)

#第二种，大概吧？？
y = 1
x= 2
z = y + x
print(y)
print(x)
while z < 100:
    print(z)
    y = x
    x = z
    z = y + x

# 3、使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上

for x in range(200):
    z = ''
    for y in range(6):
        z += random.choice('abcdefghijklmnrstopquvwxyz1234567890')
    print(z)