# 2、随机生成20个数字，并且筛选出其中最大的3个数
import string
import random


def gen_random_num(nums):
    s1 = string.digits
    lst = []
    for i in range(nums):
        num = int(''.join(random.sample(s1, 5)))
        lst.append(num)
    lst.reverse()
    return lst[-3:]
