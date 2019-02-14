#!/usr/bin/env python
#

# 1、打印正方形
#
n = 8
for i in range(1,n+1):
    if i==1 or i==n:
        print('*' * n)
    else:
        print('*' + ' ' * (n - 2) + '*')


n = 8
for i in range(n):
    if i==0 or i == n-1:
        print('*\t' * (n-1) + '*')
    else:
        print('*' + '\t' * (n-1) + '*')
    print()


# 2、九九乘法表
# 2.1
def jj(num):
    for i in range(1,num+1):
        print('%s*%s=%-4s' % (i,num,i*num), end='')
    print()
    if num < 9:
        abc(num+1)

abc(1)

# 2.2
for y in range(1,10):
    for x in range(1, y+1):
        print('%s*%s=%-4s' % (x,y,x*y), end='')
    print()



