# 1、给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0

def is_in(x, lst=None):
    if lst is None:
        lst = []
    if x in lst:
        return 1
    return 0