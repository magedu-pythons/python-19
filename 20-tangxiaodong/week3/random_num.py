# 实现随机生成200无重复激活码（或者优惠券），字符串长度大于5以上

import random

for i in range(200):
    a = ''
    for y in range(10):
        a += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    print(a)


"""
(0 + 0)

    没有解决重复优惠码的问题，请参考答案
"""

