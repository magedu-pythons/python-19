#!/usr/bin/env python
#
# 九九乘法表
def abc(num=1,order='aes'):
    for i in range(1,num+1):
        print('%s*%s=%-4s' % (i,num,i*num), end='')
    print()
    if order=='aes':
        if num < 9:
            abc(num+1)
    elif order == 'desc':
        if num > 0:
            abc(num-1,order)
    elif order == 'all':
        if num < 9:
            abc(num+1,order)
        else:
            abc(num-1,'desc')

abc(1)
abc(9,'desc')
abc(1,'all')
