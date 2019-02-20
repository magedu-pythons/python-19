import random

# 1、打乱一个排好序的list对象alist，alist=[1,2,3,4,5]

alist = [1, 2, 3, 4, 5]


def randmon_list(lst: list) -> list:
    random.shuffle(lst)
    return lst