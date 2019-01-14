#
#  作业以下面这种形式实现：
#       1、xxxxx
#       答案写这里 。。。。。
#
#       测试写这里：test .....
#
#       2、xxxxx
#       答案写这里 。。。。。
#
#       测试写这里：test .......
#

# 1、实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出 现的地址；否则，返回None。

def find_sub(s1: str, s2: str):
    """
    直接使用字符串索引方式
    :param s1:
    :param s2:
    :return:
    """
    if not s1 or not s2:
        raise ValueError('input not allow empty string')
    try:
        i = s1.index(s2)
    except ValueError:
        return None
    return i

# test

find_sub('aa', 'aab')
find_sub('cc', 'eee')

# 2、给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0

def is_in(x, lst=None):
    if lst is None:
        lst = []
    if x in lst:
        return 1
    return 0

# test

is_in('a', ['a', 'c', 'c'])
is_in('b', ['c', 'd'])